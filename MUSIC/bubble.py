from moviepy.editor import *

video = VideoFileClip("music.mp4").subclip(0,60)
result.write_videofile(music_edit.mp4,fps=12)