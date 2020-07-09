# lets learn slam!

## install Kinder

https://github.com/ethz-asl/kindr

```
cd ~/catkin_ws/src
git clone git@github.com:anybotics/kindr.git
catkin_make_isolated -C ~/catkin_ws
```

##  bug fix

```
http://packages.ros.org/ros/ubuntu/dists/xenial/InRelease の取得に失敗しました  公開鍵を利用できないため、以下の署名は検証できませんでした: NO_PUBKEY F42ED6FBAB17C654
```

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654
```

https://qiita.com/ReoNagai/items/777885f8e704028f3ab9