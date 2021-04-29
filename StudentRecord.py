from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#    return "Hello World"
@app.route("/")
def home():
    return render_template("webpage.html")

if __name__ == '__main__':
   app.run()