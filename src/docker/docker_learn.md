
# Docker勉強メモ
- docker image
- docker container
  
how to write dockerfile

ビルド
FROM: base image
RUN ：実行内容
COPY：ホストからコンテナにファイルをうつす

イメージを作成する docker image build


- -pでポート指定，ホスト：コンテナ側
- -d でバックグラウンド実行
- -itはセット，実行後中に入る，
- --rmで実行後コンテナを消す
- vで共有フォルダ設定
- 


# Docker ことはじめ


## スタート

sudo cgroupfs-mount
sudo service docker start

イメージの管理
docker image list

コンテナの管理
docker ps

docker images で REPOSITORY が <none> になっているものを削除（クライアントとデーモンAPIの両方がv1.25以降）
docker image prune

## 実行オプション

Docker imageのコマンド確認

```
docker inspect [イメージ名] --format='{{.Config.Cmd}}'
```

CMDしか表示されない。

Entrypointも確認する必要あり。

```
docker inspect [イメージ名] --format='{{.Config.Entrypoint}}'
```


bashを開く

```
docker run -it [イメージ名] /bin/bash
```

どうしてこれができるん？
https://pocketstudio.net/2020/01/31/cmd-and-entrypoint/  
イメージを実行する時、コンテナに対して何もオプションを指定しなければ、自動的に実行するコマンドを CMD 命令で指定するのがCMD。よってコンテナ実行時に引数のオプションがあれば、CMD 命令よりも実行時の引数が優先されるため。


entrypointを無理くり変えて実行
```
docker run -it --rm --entrypoint=/bin/bash x0rzkov/twint:latest -i
```


xfce4