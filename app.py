import os
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
	return "tio Teles comeu seu cu"
@app.route("/test", methods=["GET"])
def test():
	return "pika grossa"


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
