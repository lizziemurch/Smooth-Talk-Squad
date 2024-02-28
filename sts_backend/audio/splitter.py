from pydub import AudioSegment
import wave
import os

def splitter(filename, file_location) -> None:
    start=0
    end=3000
    # filenme=filename
    wavfile = wave.open(file_location)
    frames = wavfile.getnframes()
    rate = wavfile.getframerate()
    duration = frames/float(rate)
    print(duration)
    for i in range(int(duration)):
        newAudio = AudioSegment.from_wav(file_location)
        newAudio = newAudio[start:end]
        newaudname="test_"+str(i)+".wav"
        newAudio.export(os.path.join('sts_backend','audio','splits', newaudname), format="wav") #Exports to a wav file in the current path.

        start = start + 1000
        end = start + 3000
        start_seconds = start/1000
        end_seconds = end/1000
        print(f"{start_seconds}-{end_seconds}")
        if end_seconds>duration:
            break;
