from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello from vv8b6w8t Elastic Beanstalk CI-CD verification-202610231410256900"


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
