from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# IMPORT BOTH APPS
from attendance_app.main import app as attendance_app
from boarders_manager.main import app as boarders_app

# MAIN HOME APP
home_app = Flask(__name__)

@home_app.route("/")
def home():
    return render_template("home.html")

# MERGE APPS
app = DispatcherMiddleware(home_app, {
    "/attendance": attendance_app,
    "/boarders": boarders_app
})

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 5000, app, use_reloader=True)