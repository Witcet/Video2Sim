import os
from Pose2Sim.Pose2Sim import read_config_file
from Pose2Sim import Pose2Sim
from zup import zup


config_path = os.path.join('User', 'tangjie.toml')
config_dict = read_config_file(config_path)
frame_range = config_dict.get('project').get('frame_range')

# 相机标定  —— matlab
# Pose2Sim.calibrateCams(config_path)
# 姿态估计    ——openpose的bin目录下起终端
# bin\OpenPoseDemo.exe --model_pose BODY_25B --video D:\OpenSim\Video2Sim\raw-2d\cam1.avi --write_json D:\OpenSim\Video2Sim\pose-2d\pose_cam1_json


# 主角追踪-三维重建-坐标过滤
Pose2Sim.track2D(config_path)

Pose2Sim.triangulate3D(config_path)

Pose2Sim.filter3D(config_path)

zup()

