# Twitter Scraper

有用なTweetをしている人のTweet内容をスクレイピングしてデータベース化したい。

スクレイピングに使えるTwitter APIは申請時に結構面倒な作文を要求されるので面倒な作業のいらないものを探していた，

pipでインストールできるようだが，自分の散らかったPython環境だと上手く行かなかったのと，Python環境がPC毎に違うのでDockerでやることにした。

https://github.com/jonbakerfish/TweetScraper

## DockerでBuild

ホームにいって以下のビルドを試す。

```
docker build -t twitterscraper:build .
```

自分の環境では以下のようなErrorがでた。

```
Please make sure the libxml2 and libxslt development packages are installed.
```

依存関係のあるパッケージが上手くはいっていなかったので
[ここを見て](https://github.com/taspinar/twitterscraper/issues/250)
Docker FileをFixする。


### Docker memo：Create Shared Drive for Docker

https://www.virment.com/docker-sharing-folder-setup/

1. type `id` and get UID 1000
2. ...

no,no,no

you can just do it by command

## How to use

```
docker run --rm -it -v/<PATH_TO_SOME_SHARED_FOLDER_FOR_RESULTS>:/app/data twitterscraper:build <YOUR_QUERY>
```

QueryとはここではDocker環境で実行するコマンドのようだ。


- view help
```
docker run --rm -it twitterscraper:build twitterscraper --help
```


# 特定のユーザのTweetをスクレイピング


特定のユーザのTweetを抜き出すには`--user`オプションを用いる手法と`from:<USERNAME>`のクエリを指定することでも検索できる。
`--lang`で日本語を指定している。

- Donwloading1
```
docker run --rm -it -v /home/yoshi/Documents/GitHub/MyMemo/src/Twitter:/app twitterscraper:build twitterscraper slam_hub --user -o slamhub.txt --lang ja -l 1200
```

- Donwloading2

```
docker run --rm -it -v /home/yoshi/Documents/GitHub/MyMemo/src/Twitter:/app twitterscraper:build twitterscraper "from:slam_hub" -o slamhub2.json --lang ja -l 2000
```

- Donwloading3

```
docker run --rm -it -v /home/yoshi/Documents/GitHub/MyMemo/src/Twitter:/app twitterscraper:build twitterscraper "from:slam_hub" -o slamhub3.json --lang ja -l 2000 -bd 2020-01-01BB
```

もっとたくさんあるはずだが？？

# Twintを用いた解析

Twintを用いる。

環境：Docker WSL2

git clone --depth=1 https://github.com//twintproject/twint-docker
cd twint-docker/dockerfiles/latest/slim
docker pull x0rzkov/twint:latest 
alias twint="docker run -ti --rm -v $(pwd)/data:/opt/app/data x0rzkov/twint:latest-slim" 
docker-compose up -d elasticsearch kibana  
sudo apt install docker-compose 
docker network  create nw-twint



## Self try
Composeの全容がわからんので自分でもやってみる。

Dockerfileの中身はこんなん

```
FROM python:3.7-slim-stretch

MAINTAINER x0rxkov <x0rxkov@protonmail.com>

ARG TWINT_VERSION=v2.1.16

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN \
apt-get update && \
apt-get install -y \
git

RUN \
pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@v2.1.16#egg=twint

RUN \
apt-get clean autoclean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["/entrypoint.sh"]
VOLUME /twint
WORKDIR /opt/twint/data
```

普通にDockerfileを落としてきてプログラム回せば良さそう。

普通にPullして以下を実行すれば良いように見える。

```
docker pull x0rzkov/twint:latest
docker run -ti --rm -v $(pwd)/data:/opt/twint/data x0rzkov/twint:latest -u slam_hub -o slamhub_twint.json
```

- package install
- twint install
- Dockerの中でDockerを走らせる？

docker run -it --rm --entrypoint=/bin/bash x0rzkov/twint:latest -i

entrypoint≒CMDっぽい
https://qiita.com/hihihiroro/items/d7ceaadc9340a4dbeb8f



Docker imageのコマンド確認

```
docker inspect [イメージ名] --format='{{.Config.Cmd}}'
```

bashを開く

```
docker run -it [イメージ名] /bin/bash
```

