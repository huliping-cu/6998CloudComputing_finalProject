from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

#Variables to track score (Game)
score=0
total_score=10

#Variables to track steps completed (Learn)
steps_completed=0
total_steps=11

#Data in JSON
data={
    "0": {
        "id": "hs7488",
        "name": "michael scott",
        "email":"123456789",
        "profile_pic":"/static/images/woman.jpng"
    },
    "1": {
        "id": "jh8523",
        "name": "jim halpert",
        "email":"234567890",
        "profile_pic":"/static/images/woman.jpng"
    },
}





#ROUTES
@app.route('/')
def home():
   return render_template('home.html',data = data)






if __name__ == '__main__':
   app.run(debug = True)

