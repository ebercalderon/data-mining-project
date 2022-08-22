import random

from flask import jsonify, request
from flask_cors import cross_origin
from app.ml import ml
from app.info import features, questions, answers, questionWithComplete

from flask import Flask, jsonify, request

app = Flask(__name__)



# Home Page
@app.route('/')
def home():
    return "Welcome to backend - chatbot."

# [POST] Response
@app.route('/api/questions/', methods = ['POST'])
@cross_origin()
def getQuestions():
    availableFeatures = features[:]
    characterMatch = None
    classImage = ''

    if 'alreadyFeatures' in request.json:
        availableFeatures = set(availableFeatures) - set(request.json['alreadyFeatures'])
        characterMatch = ml(request.json['alreadyFeatures'], request.json['params'], request.json['answers'])
        characterMatch = characterMatch.to_dict()

        characterMatchId = 0
        for id in characterMatch['class']:
            characterMatchId = id

        print(characterMatch)
        print(characterMatch['class'][characterMatchId])

        if characterMatch['class'][characterMatchId] == 'yes':
            classImage = 'https://raw.githubusercontent.com/ebercalderon/data-mining-project/main/frontend/src/images/good.gif'
        else:
            classImage = 'https://raw.githubusercontent.com/ebercalderon/data-mining-project/main/frontend/src/images/bad.gif'

        characterMatch = {
          "name": characterMatch['class'][characterMatchId],
          "image": classImage,
          "eye_color": characterMatch['job'][characterMatchId],
          "publisher": characterMatch['education'][characterMatchId],
          "place_of_birth": characterMatch['default'][characterMatchId]
        }
    else:
        availableFeatures = set(availableFeatures) - set(questionWithComplete)

    availableFeatures = list(availableFeatures)

    if(not len(availableFeatures)):
        return jsonify(
            characterMatch = characterMatch
        )

    feature = random.choice(availableFeatures)
    param = feature
    question = questions[feature]

    if feature in questionWithComplete:
        question += characterMatch[feature] + '?'
        param = 'is_' + characterMatch[feature]

    if characterMatch:
        del characterMatch['job']
        del characterMatch['education']
        del characterMatch['default']

    return jsonify(
      feature = feature,
      param = param,
      question = question,
      answers = answers[feature],
      characterMatch = characterMatch
    )
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
