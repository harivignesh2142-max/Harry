from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "Hello everyone, It's me Harry potter"

@app.route('/contact')
def contact():
    return "Contact us at instagram anytime macha !"

@app.route('/products')
def products():
    return "neraiya iruku enga ooruku va macha."

@app.route('/services')
def services():
    return "Small chats including the best performance chats, tips, ideas"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name.capitalize()} ! ena pandra mamey ? inga ena solludhu ? Jessi Jessi nu solludha"

if __name__ == '__main__':
    app.run(port=5001, debug=True)