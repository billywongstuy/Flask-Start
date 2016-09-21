from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "No mi"

@app.route("/secret")
def secsec():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    Hello! Can you read this?
    </body>
    </html>
    '''

@app.route("/notsecret")
def something():
    return "you cannot read this"


if __name__ == "__main__":
    app.run()
