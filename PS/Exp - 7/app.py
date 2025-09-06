from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
   return "<h1>Hello from Dockerized Flask App!</h1></br><p>Name: Kshitij K Sawant</p></br><p>Subject : PS - IV</p></br><p>Experiment - 7</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
