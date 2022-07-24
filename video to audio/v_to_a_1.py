#coding=gbk
from moviepy.editor import AudioFileClip
my_audio_clip = AudioFileClip("D:/py_pro/video to audio/009公虾米.mp4")
my_audio_clip.write_audiofile("D:/py_pro/video to audio/009公虾米.mp3")
