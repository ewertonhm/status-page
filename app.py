from flask import Flask, render_template
from main import run
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def status_page():
    status = run()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render_template('index.html', status=status, timestamp=current_time)

@app.route('/health')
def health_route():
    return render_template('health.html')