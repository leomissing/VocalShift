import os
import sys
# import ffmpeg
import subprocess
print(os.listdir())


def create_folders():
    paths = ["split/", "sounds/", "results/"]
    for path in paths:
        if os.path.exists(path):
            continue
        os.makedirs(path)


def split_and_con_song(file_name):
    from src.Convertor import Convertor

    # conv = Convertor()
    # conv.convert('sounds/kino_test.mp3', 'sounds/kino_test.wav',
    #              'mp3', 'wav')
    create_folders()
    cwd = os.getcwd()
    sys.path.append(cwd + '/vocal-remover/')
    # gpu 0 - if you have one
    proc = subprocess.Popen(['python', f'{sys.path[-1]}/inference.py',
                             '--pretrained_model', f"{sys.path[-1]}/models/baseline.pth",
                             "--gpu", "-1", '--input', f"{sys.path[0]}/sounds/{file_name}.mp3", '--output_dir',
                             f"{sys.path[0]}/split"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        print(line)

    from pydub import AudioSegment
    vocal = AudioSegment.from_wav(f"split/{file_name}_Vocals.wav")
    instruments = AudioSegment.from_wav(f"split/{file_name}_Instruments.wav")
    output = instruments.overlay(vocal, position=0)
    output.export(f"results/{file_name}_overlay.mp3", format="mp3")


if __name__ == "__main__":
    split_and_con_song("kino_test.mp3")
