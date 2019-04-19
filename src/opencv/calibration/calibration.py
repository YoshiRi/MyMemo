import glob

import cv2
import numpy as np

samples = []
image_points = []
for path in glob.glob('imgs/*.png'):
    img = cv2.imread(path)
    samples.append(img)

# chessboard size
cols = 9  
rows = 6  

for img in samples:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, corners = cv2.findChessboardCorners(img, (cols, rows))
    if ret:
        image_points.append(corners)
    else:
        print('corners detection failed.')


world_points = np.zeros((rows * cols, 3), np.float32)
world_points[:, :2] = np.mgrid[:cols, :rows].T.reshape(-1, 2)
print('world_points shape:', world_points.shape)  # world_points shape: (54, 3)

for img_pt, world_pt in zip(image_points[0], world_points):
    print('image coordinate: {} <-> world coordinate: {}'.format(img_pt, world_pt))

object_points = [world_points] * len(samples)


h, w, c = samples[0].shape
ret, camera_matrix, distortion, rvecs, tvecs = cv2.calibrateCamera(
    object_points, image_points, (w, h), None, None)

print('reprojection error:\n', ret)
print('camera matrix:\n', camera_matrix)
print('distortion:\n', distortion)
print('rvecs:\n', rvecs[0].shape)
print('tvecs:\n', tvecs[0].shape)

np.savetxt("K.csv", camera_matrix, delimiter=",")
np.savetxt("dist.csv", distortion, delimiter=",")

cap.release()
cv2.destroyAllWindows()


