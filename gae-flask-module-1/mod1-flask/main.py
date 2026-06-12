import datetime
from flask import Flask, render_template, request


app = Flask(__name__)

visits = []


@app.route("/")
def root():
    user_agent = request.headers.get("User-Agent", "unknown")
    now = datetime.datetime.now(datetime.UTC).strftime("%a %b %d %H:%M:%S %Y")
    visits.insert(0, f"{now} from {user_agent}")
    del visits[10:]

    return render_template("index.html", visits=visits)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
