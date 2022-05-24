from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def Home():
    return {"status":"working"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5012")    
