import requests 
from bs4 import BeautifulSoup
import re


def getRespective(url):
	req = requests.get(url.strip())
	soup = BeautifulSoup(req.content,'html.parser')
	IsGif,IsImage,IsVideo = getGif(soup),getImage(soup),getVideo(soup)
	lists = [IsGif,IsVideo,IsImage]
	return lists

def getGif(soup):
	for i in soup.find_all('link'):
		if 'href' in i.attrs:
			if i['href'].startswith('https://i.pinimg.com'):
				return i['href']
	else:
		return False

def getImage(soup):
	for i in soup.find_all('meta'):
		if 'content' in i.attrs:
			if i['content'].startswith('https://i.pinimg.com/'):
				return i['content']
				break
	else:
		return False

def getVideo(soup):
	pattern = re.compile(r"https://v.pinimg.com/videos/[a-zA-Z0-9/]+\.mp4")
	for i in soup.find_all('script'):
		if 'id' in i.attrs:
			if i['id'] == 'initial-state':
				match = pattern.findall(i.string)
				return match
				break
	else:
		return False

#print(getRespective('https://in.pinterest.com/pin/284219426475932145/'))