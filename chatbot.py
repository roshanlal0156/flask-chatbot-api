from flask import Flask
from algorithm import Algo

app = Flask(__name__)

@app.route("/<que>")
def reply(que):
    obj = Algo()
    ans = obj.qna(que)
    return {"ans": ans}

if __name__ == "__main__":
    app.run(debug=True)
    
    