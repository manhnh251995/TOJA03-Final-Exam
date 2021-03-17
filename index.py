from flask import Flask
import os
version = os.environ.get("VERSION")
hostnamesvr = os.environ.get("HOSTNAME")

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World Python {} {} !".format(version,hostnamesvr)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
