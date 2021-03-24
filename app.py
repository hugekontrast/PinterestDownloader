from flask import *
from scrape import *

app = Flask(__name__)

@app.route('/')
def function():
	link = request.args.get("link")
	if not(link == None):
		url = getRespective(link)
		reception = {'postType':'','src':''}
		if url[1] != []:
			reception['postType'] = 'video'
			reception['src'] = url[1][0]
		else:
			reception['postType'] = 'image'
			reception['src'] = url[0]
		return render_template('index.html' , reception=reception)
	return render_template('index.html')