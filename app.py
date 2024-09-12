import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return """Hello this page has been built using the S2I feature of OpenShift with the name kulpythonapp!
    Webhook is added in GitHub to trigger Build in Openshift S2I!
    Debugging is in progress!
    Build is successful now"""

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
