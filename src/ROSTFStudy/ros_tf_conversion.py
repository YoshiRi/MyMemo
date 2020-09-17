import rospy
import geometry_msg
import tf

# Transform to homogeneous matrix
def transform2homogeneousM(tfobj):
    # Quat to euler sxyz とあるが， XYZWの順番で良い。ちょっとわかりにくくないか？
    tfeul= tf.transformations.euler_from_quaternion([tfobj.rotation.x,tfobj.rotation.y,tfobj.rotation.z,tfobj.rotation.w],axes='sxyz')
    # 並進量の記述
    tftrans = [ tfobj.translation.x,tfobj.translation.y,tfobj.translation.z]
    tfobjM = tf.transformations.compose_matrix(angles=tfeul,translate=tftrans)
    # return
    return  tfobjM

def homogeneous2transform(Mat):
    scale, shear, angles, trans, persp = tf.transformations.decompose_matrix(Mat)
    quat = tf.transformations.quaternion_from_euler(angles[0],angles[1],angles[2])
    tfobj = geometry_msgs.msg.Transform()
    tfobj.rotation.x = quat[0]
    tfobj.rotation.y = quat[1]
    tfobj.rotation.z = quat[2]
    tfobj.rotation.w = quat[3]
    tfobj.translation.x = trans[0]
    tfobj.translation.y = trans[1]
    tfobj.translation.z = trans[2]
    return tfobj
    
# Transform diff tf1 to 2

def transform_diff(tf1,tf2):
    tf1M = transform2homogeneousM(tf1)
    tf2M = transform2homogeneousM(tf2)
    return  homogeneous2transform(tf2M.dot(tf.transformations.inverse_matrix(tf1M)))
    

# Pose version も作る
def pose2homogeneousM(poseobj):
    try:
        # Quat to euler sxyz とあるが， XYZWの順番で良い。ちょっとわかりにくくないか？
        tfeul= tf.transformations.euler_from_quaternion([poseobj.orientation.x,poseobj.orientation.y,poseobj.orientation.z,poseobj.orientation.w],axes='sxyz')
        # 並進量の記述
        tftrans = [ poseobj.position.x,poseobj.position.y,poseobj.position.z]
        poseobjM = tf.transformations.compose_matrix(angles=tfeul,translate=tftrans)
        return poseobjM
    except:
        print("Input must be a pose object!")

        
def homogeneous2pose(Mat):
    scale, shear, angles, trans, persp = tf.transformations.decompose_matrix(Mat)
    quat = tf.transformations.quaternion_from_euler(angles[0],angles[1],angles[2])
    poseobj = geometry_msgs.msg.Pose()
    poseobj.orientation.x = quat[0]
    poseobj.orientation.y = quat[1]
    poseobj.orientation.z = quat[2]
    poseobj.orientation.w = quat[3]
    poseobj.position.x = trans[0]
    poseobj.position.y = trans[1]
    poseobj.position.z = trans[2]
    return poseobj

def pose_diff(p1,p2):
    p1M = pose2homogeneousM(p1)
    p2M = pose2homogeneousM(p2)
    return  homogeneous2pose(p2M.dot(tf.transformations.inverse_matrix(p1M)))
