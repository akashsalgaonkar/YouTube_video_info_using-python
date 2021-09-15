import pytube 
from pytube import YouTube
video_url = 'https://youtu.be/Q9exOeJDsGg'
video = pytube.YouTube(video_url)
print(video.title)
print(video.description)
print("video id= ",video.video_id)
print("video length= ",video.length)
print("video views= ",video.views)
print("video rating= ",video.rating)
print("video thumbnail= ",video.thumbnail_url)