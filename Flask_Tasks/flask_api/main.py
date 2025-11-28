from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={
         "harry":56,
          "ruta":87,
          "opp":29 
         }
    values=[1,marks,67]
    return jsonify(marks)

app.run(debug=True)