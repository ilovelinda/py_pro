from moviepy.editor import *

# ����50-60������� 00:00:50 - 00:00:60
video = CompositeVideoClip([VideoFileClip("videoplayback.mp4").subclip(50, 60)])

# д�������ɵ�����
video.write_videofile("done.mp4")