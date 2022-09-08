from pytube import YouTube
from pytube.cli import on_progress

print("YOUTUBE VIDEO DOWNLOADER")
print("________________________")
print()
print()

link = input("Enter video link: ")
print("Loading video...")
yt = YouTube(link)
videos = yt.streams.all()
vid = list(enumerate(videos))

for i in vid:
	print(i)
print()

strm = int(input("Select stream: "))
print("Downloading file...")
videos[strm].download()

print("Download successfull!")
