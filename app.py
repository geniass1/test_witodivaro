from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder=".")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(300), nullable=False)
    fullname = db.Column(db.String, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/script.js')
def lox():
    return render_template('script.js')


@app.route('/add', methods=['POST'])
def add():
    name = request.json['name']
    surname = request.json['surname']
    fullname = request.json['fullname']
    article = Article(name=name, fullname=fullname, surname=surname)
    db.session.add(article)
    db.session.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)  # pragma: no cover
