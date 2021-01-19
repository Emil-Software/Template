from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


class Teachers2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imgUrl= db.Column(db.String, unique=True, nullable=False)
    imgDescription = db.Column(db.String, unique=True, nullable=False)
    imgUrl = db.Column(db.String, unique=True, nullable=False)


@app.route('/teachers.html',methods=['GET','POST'])
def home():
    books=Book.query.all()
    return render_template('teachers-2.html')



if __name__=='__main__':
    app.run(debug=True)
    manager.run()