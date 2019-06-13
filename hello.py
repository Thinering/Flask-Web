from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



if __name__ == '__main__':
    app.debug = True
    app.run()
