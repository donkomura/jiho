#!/usr/bin/env python3
import datetime
import os
import argparse
from pydub import AudioSegment
from pydub.playback import play

audio_dir = "audio"
intro = "intro.wav"


def play_wav(path):
    sound = AudioSegment.from_file(path, format="wav")
    play(sound)


def main():
    parser = argparse.ArgumentParser(description='reporting time by MOE voices')
    parser.add_argument('voice', metavar='VOICE', type=str, nargs=1,
            help="voice to read time (set directory name in 'audio' dir)")
    args = parser.parse_args()

    current = os.path.dirname(__file__)

    # intro
    intro_path = os.path.join(current, audio_dir, intro)
    play_wav(intro_path)

    # jiho
    now = datetime.datetime.now()
    audio_path = os.path.join(current, audio_dir, args.voice[0])
    time_path = os.path.join(audio_path, str(now.hour) + ".wav")
    print("jiho: {} {}", time_path, now)
    play_wav(time_path)


if __name__ == '__main__':
    main()
