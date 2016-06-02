import urllib.request
import random

def Download_Web_Image(url):
    num = random.randint(1,200)
    name = str(num) + '.jpeg'
    urllib.request.urlretrieve(url, name)

#put a url of a picture from the web into the Function Below
#Example: Download_Web_Image("https://s-media-cache-ak0.pinimg.com/236x/e9/3d/23/e93d233338465334f5263f2b311252bd.jpg")
# Make sure you put qoutes at the beginning and end of the url
Download_Web_Image("https://s-media-cache-ak0.pinimg.com/236x/e9/3d/23/e93d233338465334f5263f2b311252bd.jpg")