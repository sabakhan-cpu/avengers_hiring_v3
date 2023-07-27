from flask import Flask, render_template, jsonify
#

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        "title": "Iron Man",
        "location":"Chicago, New York",
        "Salary": "130 gold coin/month",

    },
    {'id': 2,
     "title": "Thor",
     "location":"Asgard,Planet",
     "Salary": "135 gold coin/month",
     },
    {
        'id': 3,
        "title": "Black Widow",
        "location": "Volgograd, Russian SFSR, USSR",
        "Salary": "125 gold coin/month",
    }
]


@app.route("/")
def home():
    return render_template('index.html', jobs=JOBS)


@app.route('/api/jobs/')
def call():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
