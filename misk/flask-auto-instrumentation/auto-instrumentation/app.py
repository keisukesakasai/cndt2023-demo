from flask import Flask, request

app = Flask(__name__)
print(app)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    return "served"


if __name__ == "__main__":
    app.run(port=8081)