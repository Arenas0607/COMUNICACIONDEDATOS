from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal (login)
@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
