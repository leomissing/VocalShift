from pydub import AudioSegment

class Convertor:
    
    def __init__(self):
        pass
    def convert(self, src, dst, input_format, output_format):
        sound = AudioSegment.from_file(src, format=input_format)
        sound.export(dst, format=output_format)
        print('Complete successful in dst')
