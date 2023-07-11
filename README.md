# Video2Sim
从多相机视频到Opensim模型运动

下载后在项目根目录下创建pose-2d文件夹

在OpenPose/bin文件夹下起终端运行：
bin\OpenPoseDemo.exe --model_pose BODY_25B --video D:\OpenSim\Video2Sim\raw-2d\cam1.avi --write_json D:\OpenSim\Video2Sim\pose-2d\pose_cam1_json

然后运行main.py，最终生成的pose-3d/test...文件即为需要的trc文件，导入opensim做逆运动学分析

backup文件夹里的kaiwu文件夹下为实验室的测试视频和相机校准文件
AIST文件夹下为一个公开舞蹈数据集的一次动作视频和相机校准文件

User文件夹下的toml配置文件中的参数含义可以查阅官方文档，以及pose2sim库中的代码