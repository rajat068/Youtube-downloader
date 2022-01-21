from pytube import YouTube



YouTube("https://youtu.be/QohcuHVBMQ4").streams.first().download()