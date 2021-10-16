from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///course.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class course(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1000),nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.course}"

@app.route('/')
def index():
    return render_template('index.html')
    return 'hello'

@app.route('/contact')
def contact():
    return '1234567890, /n linkedin'

if  __name__ == '__main__':
    app.run(debug=True, port=8080 )    