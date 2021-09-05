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
    current = os.path.dirname(__file__)
    audio_path = os.path.join(current, audio_dir)

    # intro
    path_intro = os.path.join(audio_path, intro)
    play_wav(path_intro)

    # jiho
    now = datetime.datetime.now()
    path_jiho = os.path.join(audio_path, str(now.hour) + ".wav")
    print("jiho: {} {}", path_jiho, now)
    play_wav(path_jiho)


if __name__ == '__main__':
    main()
