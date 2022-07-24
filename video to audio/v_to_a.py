import moviepy.editor as mp

def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    return my_clip

if __name__ == "__main__":
    file_path = r'./huozhe.mp4'
    my_clip = extract_audio(file_path)
    my_clip.audio.write_audiofile(f'huozhe.wav')
