# jiho

waifu が時刻をお知らせしてくれるスクリプト

 が時刻をお知らせしてくれるスクリプト

## Requirements

### 依存パッケージのインストール
```sh
$ pip3 install -r requirements.txt
```

## usage

```
usage: main.py [-h] VOICE

reporting time by MOE voices

positional arguments:
  VOICE       voice to read time (set directory name in 'audio' dir)

optional arguments:
  -h, --help  show this help message and exit
```

### VOICE

* [ミリアル](./audio/millial)
* [榛名](./audio/haruna)

### crontab

```sh
$ crontab -l
SHELL=/bin/bash
0 */1 * * * /home/kazuki/scripts/jiho/cron-jiho.sh
```

## 利用した音源

* ミリアル @ [CoeFont Studio](https://coefont.studio/)
* [榛名 時報ボイス](https://www.youtube.com/watch?v=1XMbhQxGmGk)
* [ぴんぽんぱんぽーん【初音ミク】](https://commons.nicovideo.jp/material/nc149299)

