# lets learn slam!

## install Kinder

https://github.com/ethz-asl/kindr

```
cd ~/catkin_ws/src
git clone git@github.com:anybotics/kindr.git
catkin_make_isolated -C ~/catkin_ws
```

##  bug fix
- bug fix
- https://server.etutsplus.com/apt-get-404-not-found/

- key 
```
http://packages.ros.org/ros/ubuntu/dists/xenial/InRelease の取得に失敗しました  公開鍵を利用できないため、以下の署名は検証できませんでした: NO_PUBKEY F42ED6FBAB17C654
```

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654
```

https://qiita.com/ReoNagai/items/777885f8e704028f3ab9

## add catkin build

```
sudo apt install python-catkin-tools
```

```
catkin clean # clean all builds
catkin build
```

## build rovio and run

https://github.com/ethz-asl/rovio

```
catkin build rovio --cmake-args -DCMAKE_BUILD_TYPE=Release
```

NEED euroc mav dataset to following place
/home/michael/datasets/euroc/01_easy/dataset.bag

2.5GB ... orz
it's too large.

## Vim Setting
無変換を半角変換にした。
以下のサイトで自動設定したほうがよいかもしれない。
https://endaaman.me/-/linux_keyboard_config

```
dconf write /org/gnome/desktop/input-sources/xkb-options "['caps:escape']"
```

Ctrl+CがEscぽいのでなんとかなりそう。

ここの設定を試してみた。[](https://qiita.com/matsuo7005/items/7aa5acc4820dc786eee4)