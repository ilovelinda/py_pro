#coding=gbk
# ��Ƶ�ü���ϼ�
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import concatenate_audioclips

a = AudioFileClip('bgfcmf.mp3')  #�����ļ�
# b = AudioFileClip('bgfcmf.mp3')  #�����ļ�
# c = AudioFileClip('bgfcmf.mp3')  #�����ļ�
audio1 = AudioFileClip('001���ϵ��¸�������.mp3')
audio2 = AudioFileClip('002��÷Ϸ-С����.mp3')
audio3 = AudioFileClip('003�໨��-������.mp3')
audio4 = AudioFileClip('004����-dj.mp3')
audio5 = AudioFileClip('005ˮ��DJ.mp3')
audio6 = AudioFileClip('006���ǵ��.mp3')
audio7 = AudioFileClip('007ҰĦ��.mp3')
audio8 = AudioFileClip('008��������.mp3')
audio9 = AudioFileClip('009��Ϻ��.mp3')
audio10 = AudioFileClip('010�����ж���������.mp3')
audio11 = AudioFileClip('011����Ů��-��.mp3')
audio12 = AudioFileClip('011�����ǵ���˫�� - DJR7 ������.mp3')
audio13 = AudioFileClip('012����-dj.mp3')
audio14 = AudioFileClip('013������-dj.mp3')
audio15 = AudioFileClip('014������.mp3')
audio16 = AudioFileClip('015������Ե-dj.mp3')
audio17 = AudioFileClip('016���˰�-��ѩ��.mp3')
audio18 = AudioFileClip('017����ˮ��-dj.mp3')
audio19 = AudioFileClip('018ǧ���һ��-dj.mp3')
audio20 = AudioFileClip('019����ħ����-dj.mp3')
audio21 = AudioFileClip('020���.mp3')
audio22 = a.subclip(3108,3875)   #����0~204��

# audio2 = b.subclip(5,204)   #����5~204��
# audio3 = c.subclip(5,204)   #����5~204��
audiocct = concatenate_audioclips([audio1,audio2,audio3,audio4,audio5,audio6,audio7,audio8,audio9,audio10,audio11,audio12,audio13,audio14,audio15,audio16,audio17,audio18,audio19,audio20,audio21,audio22]) # �ϲ�3����Ƶ
audiocct.write_audiofile('�����~~~~~�����˸�-DJ�ϼ�-������~~~~~.mp3') #���
#audio1.write_audiofile('abc1.mp3') #���


