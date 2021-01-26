
# import sys,os
# def mix_wav(path):
#       cmd = 'ffmpeg'
#       for filename in os.listdir(path) : #os.listdir(path)打印出路径中的所有文件
#             cmd = cmd + ' -i ' + filename
#       cmd = cmd + " -filter_complex '[0:0] [1:0] [2:0] [3:0] [4:0] [5:0] [6:0] [7:0] [8:0]
#                  concat=n=9:v=0:a=1 [a]' -map [a] /" +'output.wav'
#       os.system(cmd)
#
# mix_wav(sys.argv[1])  不行🚫