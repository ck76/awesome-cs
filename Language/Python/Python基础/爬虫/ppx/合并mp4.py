# 主要是需要moviepy这个库
from moviepy.editor import *
from natsort import natsorted
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import os

path = "/Volumes/TOSHIBA/ppx/2/untitled folder"
# qichche
#   | merge1
#       | video1.mp4    
#       | video2.mp4
#   | merge2
#       | video1.mp4
#       | video2.mp4
# =======================
# qichche
#   | merge1.mp4
#   | merge2.mp4
# 访问 qichche 文件夹 (假设视频都放在这里面)
for name in os.listdir(path):
    L = []

    for root, dirs, files in os.walk(path + '/' + name):
        # 按文件名排序
        files = natsorted(files)
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp4
            if str(file).endswith('.mp4'):
                # 拼接成完整路径
                filePath = path + '/' + name + '/' + str(file)
                # 载入视频
                print(filePath)
                video = VideoFileClip(filePath)
                print("video time: %s, width: %s, height: %s, fps: %s" % (video.duration, video.w, video.h, video.fps))
                # 添加到数组
                L.append(video)

    # #拼接视频
    final_clip = concatenate_videoclips(L, method='compose')
    # #生成目标视频文件
    # final_clip.to_videofile(path+'/'+name+'.mp4', fps=24, remove_temp=False)
    final_clip.write_videofile(path + '/' + name + '.mp4')
