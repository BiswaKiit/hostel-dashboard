from flask import Flask, render_template, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# IMPORT BOTH APPS
from attendance_app.main import app as attendance_app
from boarders_manager.main import app as boarders_app

# MAIN HOME APP
home_app = Flask(__name__)

# HOME PAGE
@home_app.route("/")
def home():
    return render_template("home.html")

# MANIFEST
@home_app.route("/manifest.json")
def manifest():
    return send_from_directory("static", "manifest.json")

# SERVICE WORKER
@home_app.route("/service-worker.js")
def service_worker():
    return send_from_directory("static", "service-worker.js")

# APPLE / ANDROID ICON
@home_app.route("/logo.png")
def logo():
    return send_from_directory("static", "logo.png")

# MERGE APPS
app = DispatcherMiddleware(home_app, {
    "/attendance": attendance_app,
    "/boarders": boarders_app
})

if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple(
        "0.0.0.0",
        5000,
        app,
        use_reloader=True,
        use_debugger=True
    )