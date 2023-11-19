from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/contatti")
def contatti():
    return "Contattaci!"

@app.errorhandler(404)
def page_not_found(error):
    return "page_not_found", 404

if __name__=='__main__':
	app.run(debug=True)