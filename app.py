from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/student'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    pet = db.Column(db.String(50), nullable=False)
    staying_christmas = db.Column(db.String(5))  # yes/no

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')  # your HTML file

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    pet = request.form.get('pets')
    staying = request.form.get('option')

    new_student = Student(
        fname=fname,
        lname=lname,
        pet=pet,
        staying_christmas=staying
    )
    db.session.add(new_student)
    db.session.commit()
    return f"Saved {fname} {lname} successfully!"

if __name__ == '__main__':
    app.run(debug=True)
