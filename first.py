import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__,template_folder="public",static_folder="public")

def get_weather(city):
    req = requests.get(f"https://www.google.com/search?client=firefox-b-d&q=Weather+{city}",headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    })
    soup = BeautifulSoup(req.text,'html.parser')
    return {
        "location": soup.select("#wob_loc")[0].get_text(),
        "time": soup.select("#wob_dts")[0].get_text(),
        "description": soup.select("#wob_dc")[0].get_text(),
        "image": soup.select("#wob_tci")[0].get_attribute_list("src"),
        "temperature": soup.select("#wob_tm")[0].getText()+" C",
        "humidity": soup.select("#wob_hm")[0].getText(),
        "precipitation": soup.select("#wob_pp")[0].getText(),
        "wind": soup.select("#wob_ws")[0].getText()
    }

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route("/api/<city>")
def getweather(city):
    return get_weather(city)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
