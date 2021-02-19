import flask
import array
import json
from flask import Flask, request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
from collections import defaultdict
generes = {}
reviews = {}
release_year = {}
movieNames = []
critics = []
users = []
userReviewonspc = {}

def criticsUpdate(username):
    for user in users:
        if username == user:
            userReviewonspc[username] += 1
@app.route('/addReviews', methods=['POST'])
def add_reviews(request):
    content = request.json()#(silent=True)
    username = content['username']  
    movieName = content['movieName']
    rating = content['rating']
    if (username in users) and (username not in critics):   
        for movie in reviews.keys():
            if movie == movieName:
                reviews[movie] = rating
        criticsUpdate(username)
    if (username in users)and(username in critics):
        for movie in reviews.keys():
            if movie == movieName:
                reviews[movie] = 2 * rating
    print(generes,users,userReviewonspc)
    return jsonify({"message":"Success"})
@app.route('/addMovie', methods=['POST'])
def add_movie(request):
    content = request.json()
    moviename = content['movieName']
    year = content['year']
    genere = content['genere']
    movieNames.append(moviename)
    generes[moviename] = genere
    release_year[moviename] = year
    reviews[moviename] = None
    print(generes, movieNames,year)
    return jsonify({"message":"Success"})
@app.route('/addUsers', methods=['POST'])
def add_users(request):
    content = request.json(silent=True)
    username = content['username'] 
    users.append(username)
    print(users)
    return jsonify({"message":"Success"})
if __name__ == '__main__':
    app.run(host= '127.0.0.8000',debug=True)
