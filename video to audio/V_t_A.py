from moviepy.editor import *

# 剪辑50-60秒的音乐 00:00:50 - 00:00:60
video = CompositeVideoClip([VideoFileClip("videoplayback.mp4").subclip(50, 60)])

# 写入剪辑完成的音乐
video.write_videofile("done.mp4")