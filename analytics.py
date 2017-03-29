import datetime
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def analytics():
    with open('logfile.txt', 'a') as f:
        currentDate = datetime.datetime.now()
        f.write(str(currentDate) + " => " + str(request.remote_addr) + "\n")
    return ""

if __name__ == "__main__":
    app.run("0.0.0.0", 33214)
