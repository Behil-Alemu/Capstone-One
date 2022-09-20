from email.mime import image
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User, Post,Likes,Inspiration
import json
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



connect_db(app)
db.create_all()

# API_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1 "

# def search_art(searched):
#     res = requests.get(f"{API_BASE_URL}/search?hasImages=true&q=Paintings&p={searched}")
#     data = res.json()
#     image= data["objectIDs"][0]["primaryImage"]
#     return image

# @app.route('/')
# def show_search_form():
#     return render_template("base.html")


# @app.route('/show_searched_art')
# def get_art():
#     searched = request.args["image"]
#     image_url = search_art(searched)
#     # import pdb; pdb.set_trace()
#     return render_template('base.html', image_url=image_url)

# for i in range(len.lenghtofAPI)
# api url with object id randrange(length)


response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=Paintings&p=African")
data = response.json()
url = data["objectIDs"][0]



res_id = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/{url}")

data_url = res_id.json()
image_URL= data_url["primaryImage"]
