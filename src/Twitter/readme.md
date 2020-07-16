# Twitter Scraper

## Docker Build

```
docker build -t twitterscraper:build .
```

Error

```
Please make sure the libxml2 and libxslt development packages are installed.
```

[ここを見てFix](https://github.com/taspinar/twitterscraper/issues/250)


Done

## Create Shared Drive for Docker

https://www.virment.com/docker-sharing-folder-setup/

1. type `id` and get UID 1000
2. ...

no,no,no

you can just do it by command

## How to use

```
docker run --rm -it -v/<PATH_TO_SOME_SHARED_FOLDER_FOR_RESULTS>:/app/data twitterscraper:build <YOUR_QUERY>
```

Query means the command. Ok.

- view help
docker run --rm -it -v /home/yoshi/Documents/GitHub/MyMemo/src/Twitter:/app twitterscraper:build twitterscraper --help

- Donwloading
docker run --rm -it -v /home/yoshi/Documents/GitHub/MyMemo/src/Twitter:/app twitterscraper:build twitterscraper slam_hub --user -o slamhub.txt --lang ja -l 1200

more ?