# how to download image through python

import requests

url = ("https://imgs.search.brave.com/ravWHqSFuqCMsIKIEb7yDdwdK9zDRTFoGl3mFcF01U8/rs:fit:860:0:0/g:ce/"
       "aHR0cHM6Ly90aGVo/YXBweXB1cHB5c2l0/ZS5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMTcvMTIvcmVk/NC5qcGc")

response = requests.get(url)
# print(response.content)
with open("img.jpg", "wb")as file:
    file.write(response.content)