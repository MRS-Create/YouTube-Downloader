from pytube import Channel

print("YOUTUBE CHANNEL DOWNLOADER")
print("__________________________")
print()
print()

c = Channel(input("Enter channel link: "))

print(f'Downloading: {c.channel_name}')

for video in c.videos:
	video.streams.first().download()

print("Download succesfull!")
