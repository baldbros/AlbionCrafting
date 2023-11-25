from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    print('hello world!')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Albion Online Data API
API_URL = "https://east.albion-online-data.com/api/v2/stats/prices/"
