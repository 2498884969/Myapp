from flask import render_template
from app import app


@app.route('/')             # Flask 创建的app
@app.route('/index')
def index():
    user = {'nickname': 'Migue'}  # fake user
    return render_template("index_if1.html", user=user)
