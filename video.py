# import os
# os.system("echo Hello from the other side!")

# ffmpeg -r 1/5 -i img%03d.jpeg -c:v libx264 -vf "fps=25,format=yuv420p" -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" out.mp4

import subprocess

list_dir = subprocess.Popen(["ffmpeg", "-r", "5", "-i", "%d.jpg", "-i", "tobu.mp3", "-c:v", "libx264", "-vf", "fps=25,format=yuv420p", "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", "out.mp4"])
list_dir.wait()

