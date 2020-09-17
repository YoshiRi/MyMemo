#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 geometry_msgs/PoseStamped.msg型メッセージを2つ受信し，その間の姿勢の差を収集，平均化して出力する。

Author(s): Y. Ri
Copyright 2020-2020 IHI Corporation
"""

import rospy
from geometry_msgs.msg import PoseStamped
import tf
import tf2_ros
import message_filters

class GetPoseErr:
    """
    calc attitude diff in PoseStamped and PoseStamped
    """

    def __init__(self):
        """
        コンストラクタ
        """
        # 終了処理を定義する
        # rospy.on_shutdown(self.__shutdown_sequence)


        # parameterの初期化
        self.has_error = False
        self.__sub_type = rospy.get_param('~sub_type', "pose") # pose

        # subするトピック名
        self.__sub_topic_name1 = rospy.get_param('~sub_topic_name1', "/mavros/local_position/pose")
        self.__sub_topic_name2 = rospy.get_param('~sub_topic_name2', "/mavros/vision_pose/pose")
        #self.__sub_topic_name2 = rospy.get_param('~sub_topic_name2', "/mavros/local_position/pose")
        
        #/cam_t265_1/fisheye1/image_raw

        # pubするトピック名
        self.__pose_topic_name = rospy.get_param('~pose_topic_name', "/att_diff")

        # pubするframe_id
        self.__pose_frame = rospy.get_param('~pose_frame', "map")
        
        # publisherの初期化
        self.__pub_pose = rospy.Publisher(self.__pose_topic_name, PoseStamped, queue_size=1)
        # subscriberの初期化
        if self.__sub_type == "pose":
            pose1_sub = message_filters.Subscriber(self.__sub_topic_name1, PoseStamped)
            pose2_sub = message_filters.Subscriber(self.__sub_topic_name2, PoseStamped)
            # 30msの違いを許容する
            ts = message_filters.ApproximateTimeSynchronizer([pose1_sub, pose2_sub], 10,0.3)
            ts.registerCallback(self.__sub_pose_callback)
        else:
            rospy.logfatal("Set sub_type 'pose'.")
            rospy.signal_shutdown("Shutdown node")
        self.__listener = tf.TransformListener()
        # 各種設定が完了するまでちょっと待つ
        rospy.sleep(1)
        rospy.logdebug("Get Err Node Activated!")
        print("Get Err Node Activated with ", self.__sub_topic_name1, self.__sub_topic_name2)

    def run(self):
        """
        クラスのメイン関数
        """
        # サブスクライブの処理しかしないので待機
        rospy.spin()


    def __sub_pose_callback(self, pose1, pose2):
        """
        subscribe時のcallback
        :param pose: PoseStamped
        """
        __pub_message,e = self.calc_pose_err(pose1, pose2)
        if e is not None:
            # Error Process
            rospy.logerr("Error in calc pose diff!!")
        # Publish
        self.__pub_pose.publish(__pub_message)
    


    def calc_pose_err(self,pose1,pose2):
        """
        get error between two pose
        input posestamped x2
        output posestamped x1
        """
        __new_message = PoseStamped()
        __new_message.header = pose1.header # 早い方に合わせる？
        __new_message.pose = pose1.pose
        
        # For debug
        # print(pose1.header.stamp, pose2.header.stamp)
        
        return __new_message,None
        
        
def main():
    # ノードを起動する
    # 同じ機能を持つ複数のノードを作成する可能性があるので，init_nodeはクラスの外でする
    rospy.init_node('get_pose_diff')
    # ノードが起動するまでちょっと待つ
    # ノードの起動が完了していないと，パラメータをセットできなかったりする
    rospy.sleep(1)
    # インスタンスを作成する
    convert_to_pose = GetPoseErr()
    # runする
    convert_to_pose.run()


if __name__ == '__main__':
    # ここにべた書きすると，外からこのファイルのメイン処理が呼び出せない
    # 外部から呼べるように，main関数を作るのがよい
    main()
