# from pydub import AudioSegment
# import struct
# sound = AudioSegment.from_file("a.mp3", format = 'aac', duration=1000)
# # get raw audio data as a bytestring
# raw_data = sound.raw_data
# print(raw_data)
# # from pytube import YouTube
# # import os
# # def downY(i):
# #     yt = YouTube(i)
# #     video = yt.streams.filter(only_audio=True).first()
# #     destination = "D:\AudioBooks"
# #     out_file = video.download(output_path=destination)
# #     base, ext = os.path.splitext(out_file)
# #     new_file = base + '.mp3'
# #     os.rename(out_file, new_file)
# # downY('https://www.youtube.com/watch?v=v6REYffqUko')
# import audio2numpy as a2n
# fs = "a.mp3"
# signal, sampling_rate = a2n.audio_from_file(fs, duration=2)
# for i in range(0, len(signal), 4410):
#     a = 0
#     b = 0
#     for j in range(i,i+4410):
#         a = a + signal[j][0]
#         b = b + signal[j][1]
#     print(str(a) + ' ' + str(b))
import requests
from bs4 import BeautifulSoup
import time
import ssl
# proxy = {
#     'http': 'http://87.101.94.82:8080',
#     'https': 'http://87.101.94.82:8080',
# }
r = requests.get('https://hdm.to/wrong-turn-2021/',)
print(r.text)