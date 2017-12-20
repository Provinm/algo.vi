import math
import numpy
import pyaudio

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency=440, length=0.1, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))
    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)
    # stream = p.open(format=pyaudio.paFloat32,
    #             channels=1, rate=40000, output=1)
    # print(vars(stream))
    # f = [256, 288, 320, 341, 384, 426, 480]
    # # play_tone(stream, frequency=480)
    # for i in f:
    i = 300
    play_tone(stream, frequency=i)

    stream.close()
    p.terminate()