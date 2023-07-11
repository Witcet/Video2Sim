import os
import shutil


def rename_video(source_folder):
    destination_folder = 'raw-2d'  # 目标文件夹路径

    # 确保目标文件夹存在
    os.makedirs(destination_folder, exist_ok=True)

    # 遍历源文件夹中的文件
    for filename in os.listdir(source_folder):
        if filename.endswith('671.avi'):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, 'cam1.avi')
            shutil.copy(source_file, destination_file)

    for filename in os.listdir(source_folder):
        if filename.endswith('264.avi'):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, 'cam2.avi')
            shutil.copy(source_file, destination_file)

    for filename in os.listdir(source_folder):
        if filename.endswith('251.avi'):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, 'cam3.avi')
            shutil.copy(source_file, destination_file)

    for filename in os.listdir(source_folder):
        if filename.endswith('676.avi'):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, 'cam4.avi')
            shutil.copy(source_file, destination_file)


if __name__ == "__main__":
    shutil.rmtree("raw-2d")
    shutil.rmtree("pose-2d")
    # shutil.rmtree("pose-2d-tracked")
    # shutil.rmtree("pose-3d")

    os.makedirs("raw-2d")
    os.makedirs("pose-2d")

    rename_video(r"C:\Users\29018\Desktop\实验方案\record_video\20230620\output\t909_1")
    # video_folder = r"C:\Users\29018\Desktop\20230620\output"
    # each_test_folder = os.listdir(video_folder)
    # for etf in each_test_folder:
    #     rename_video(etf)
