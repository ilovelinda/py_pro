#coding=gbk
# 音频裁剪与合集
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import concatenate_audioclips

a = AudioFileClip('bgfcmf.mp3')  #读入文件
# b = AudioFileClip('bgfcmf.mp3')  #读入文件
# c = AudioFileClip('bgfcmf.mp3')  #读入文件
audio1 = AudioFileClip('001天上掉下个林妹妹.mp3')
audio2 = AudioFileClip('002黄梅戏-小潘潘.mp3')
audio3 = AudioFileClip('003青花瓷-咻咻满.mp3')
audio4 = AudioFileClip('004活着-dj.mp3')
audio5 = AudioFileClip('005水手DJ.mp3')
audio6 = AudioFileClip('006星星点灯.mp3')
audio7 = AudioFileClip('007野摩托.mp3')
audio8 = AudioFileClip('008天若有情.mp3')
audio9 = AudioFileClip('009公虾米.mp3')
audio10 = AudioFileClip('010风中有朵雨做的云.mp3')
audio11 = AudioFileClip('011大哥的女人-娅娅.mp3')
audio12 = AudioFileClip('011让我们荡起双桨 - DJR7 抖音版.mp3')
audio13 = AudioFileClip('012渡情-dj.mp3')
audio14 = AudioFileClip('013白龙马-dj.mp3')
audio15 = AudioFileClip('014孤勇者.mp3')
audio16 = AudioFileClip('015金玉良缘-dj.mp3')
audio17 = AudioFileClip('016落了白-蒋雪儿.mp3')
audio18 = AudioFileClip('017梦里水乡-dj.mp3')
audio19 = AudioFileClip('018千年等一回-dj.mp3')
audio20 = AudioFileClip('019他会魔法吧-dj.mp3')
audio21 = AudioFileClip('020清空.mp3')
audio22 = a.subclip(3108,3875)   #剪切0~204秒

# audio2 = b.subclip(5,204)   #剪切5~204秒
# audio3 = c.subclip(5,204)   #剪切5~204秒
audiocct = concatenate_audioclips([audio1,audio2,audio3,audio4,audio5,audio6,audio7,audio8,audio9,audio10,audio11,audio12,audio13,audio14,audio15,audio16,audio17,audio18,audio19,audio20,audio21,audio22]) # 合并3个音频
audiocct.write_audiofile('最火火火~~~~~车载嗨歌-DJ合集-嗨嗨嗨~~~~~.mp3') #输出
#audio1.write_audiofile('abc1.mp3') #输出


