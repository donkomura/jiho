#!/usr/bin/env python3
import datetime
import os
from pydub import AudioSegment
from pydub.playback import play

audio_dir = "audio"
intro = "intro.wav"

def play_wav(path):
    sound = AudioSegment.from_file(path, format="wav")
    play(sound)

def main():
    current = os.getcwd()
    now = datetime.datetime.now()

    # intro
    path_intro = current + "/" + audio_dir + "/" + intro
    play_wav(path_intro)

    # jiho
    path_jiho = current + "/" + audio_dir + "/" + str(now.hour) + ".wav"
    print("jiho: {}", path_jiho)
    play_wav(path_jiho)

if __name__ == '__main__':
    main()
