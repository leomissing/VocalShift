import os
import glob
import json
import copy
import io
from pathlib import Path

from inference import infer_tool
from inference import slicer
from inference.infer_tool import Svc
import soundfile
import numpy as np


os.chdir("/content/so-vits-svc")

MODELS_DIR = "models"
OUTPUTS_DIR = "results"
INPUTS_DIR = "raw"

slice_db = -40
wav_format = "wav"


def get_speakers():
    speakers = []
    for _, dirs, _ in os.walk(MODELS_DIR):
        for folder in dirs:
            cur_speaker = {}
            # Look for G_****.pth
            g = glob.glob(os.path.join(MODELS_DIR, folder, "G_*.pth"))
            if not len(g):
                print("Skipping " + folder + ", no G_*.pth")
                continue
            cur_speaker["model_path"] = g[0]
            cur_speaker["model_folder"] = folder

            # Look for *.pt (clustering model)
            clst = glob.glob(os.path.join(MODELS_DIR, folder, "*.pt"))
            if not len(clst):
                print("Note: No clustering model found for " + folder)
                cur_speaker["cluster_path"] = ""
            else:
                cur_speaker["cluster_path"] = clst[0]

            # Look for config.json
            cfg = glob.glob(os.path.join(MODELS_DIR, folder, "*.json"))
            if not len(cfg):
                print("Skipping " + folder + ", no config json")
                continue
            cur_speaker["cfg_path"] = cfg[0]
            with open(cur_speaker["cfg_path"]) as f:
                try:
                    cfg_json = json.loads(f.read())
                except Exception as e:
                    print("Malformed config json in " + folder)
                for name, i in cfg_json["spk"].items():
                    cur_speaker["name"] = name
                    cur_speaker["id"] = i
                    if not name.startswith("."):
                        speakers.append(copy.copy(cur_speaker))

        return sorted(speakers, key=lambda x: x["name"].lower())


def add_padding(audio_sr, data):
    pad_len = int(audio_sr * 0.5)
    data = np.concatenate([np.zeros([pad_len]), data, np.zeros([pad_len])])
    return data


def get_out_audio(out_audio, svc_model):
    _audio = out_audio.cpu().numpy()
    pad_len = int(svc_model.target_sample * 0.5)
    _audio = _audio[pad_len:-pad_len]
    return _audio


def choice_speaker():
    speakers = get_speakers()
    speaker_list = [x["name"] for x in speakers]

    # TODO
    print(speaker_list)
    speaker_name = input()

    speaker = next(x for x in speakers if x["name"] == speaker_name)
    return speaker


def convert(wav_path, speaker):
    trans = 12
    cluster_ratio_tx = 0.0
    noise_scale_tx = 0.4
    auto_pitch_ck = False

    svc_model = Svc(
        speaker["model_path"],
        speaker["cfg_path"],
        cluster_model_path=speaker["cluster_path"],
    )

    wav_name = Path(wav_path).stem
    chunks = slicer.cut(wav_path, db_thresh=slice_db)
    audio_data, audio_sr = slicer.chunks2audio(wav_path, chunks)

    audio = []
    for slice_tag, data in audio_data:
        length = int(np.ceil(len(data) / audio_sr * svc_model.target_sample))

        if slice_tag:
            _audio = np.zeros(length)
        else:
            data = add_padding(audio_sr, data)

            raw_path = io.BytesIO()
            soundfile.write(raw_path, data, audio_sr, format="wav")
            raw_path.seek(0)
            _cluster_ratio = 0.0
            if speaker["cluster_path"] != "":
                _cluster_ratio = float(cluster_ratio_tx)

            out_audio, out_sr = svc_model.infer(
                speaker["name"],
                trans,
                raw_path,
                cluster_infer_ratio=_cluster_ratio,
                auto_predict_f0=auto_pitch_ck,
                noice_scale=float(noise_scale_tx),
            )

            _audio = get_out_audio(out_audio, svc_model)
        audio.extend(list(infer_tool.pad_array(_audio, length)))

    res_path = os.path.join(
        "/content/so-vits-svc",
        OUTPUTS_DIR,
        f"{wav_name}_{trans}_key_" f'{speaker["name"]}.{wav_format}',
    )
    print("Res path:", res_path)
    soundfile.write(res_path, audio, svc_model.target_sample, format=wav_format)


def inference():
    os.makedirs(os.path.join("/content/so-vits-svc/", OUTPUTS_DIR), exist_ok=True)

    wav_path = glob.glob(os.path.join("/content/so-vits-svc/", INPUTS_DIR) + "/*.*")[0]
    assert wav_path.endswith(".wav")

    speaker = choice_speaker()
    convert(wav_path, speaker)


if __name__ == "__main__":
    inference()
