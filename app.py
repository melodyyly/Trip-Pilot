from flask import Flask, render_template, request, jsonify

from agents.trip_agent import TripAgent

app = Flask(__name__)

agent = TripAgent()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    result = agent.run(message)

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )