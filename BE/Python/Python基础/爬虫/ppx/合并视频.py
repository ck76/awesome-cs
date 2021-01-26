import ffmpeg
import moviepy
import natsort

# 主要是需要moviepy这个库
from moviepy.editor import *
import os

path = "/Volumes/TOSHIBA/ppx/2/untitled folder/"
os.chdir(path)
# 定义一个数组
L = []

# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk(path):
    # 按文件名排序
    files.sort()
    # 遍历所有文件
    for file in files:
        print(file)
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            print(filePath)
            video = VideoFileClip(filePath)
            # 添加到数组
            L.append(video)

# 拼接视频
final_clip = concatenate_videoclips(L,method='compose')

# 生成目标视频文件
# final_clip.write_videofile(path + "result.mp4", fps=24, remove_temp=False)
final_clip.write_videofile(path + "result.mp4")