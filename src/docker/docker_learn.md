
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