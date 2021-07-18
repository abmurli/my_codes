from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [ 
    "https://images-na.ssl-images-amazon.com/images/I/51Ks92NyjeL._SX425_.jpg",
    "https://cmkt-image-prd.global.ssl.fastly.net/0.1.0/ps/2166420/1160/772/m1/fpnw/wm0/1-.png?1485112101&s=61e57d19aa3abfa6cb84ecf26f024b56",
    "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
