from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    f_name=db.Column(db.String(50))
    l_name=db.Column(db.String(50))
    username=db.Column(db.String(50))
    e_mail=db.Column(db.String(50))
    adress=db.Column(db.String(50))
    adress_2=db.Column(db.String(50))

@app.route('/')
def index():
    users=User.query.all()
    # select * from User
    return render_template('index.html',users=users)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        user=User(
            f_name=request.form['f_name'],
            l_name=request.form['l_name'],
            username=request.form['username'],
            e_mail=request.form['e_mail'],
            adress=request.form['adress'],
            adress_2=request.form['adress_2']
        )
        db.session.add(user)
        # insert into User(f_name,l_name) values(request.form['f_name'],request.form['l_name'])
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    user=User.query.get(id)
    if request.method=='POST':
        user.f_name=request.form['f_name']
        user.l_name=request.form['l_name']
        user.username=request.form['username']
        user.e_mail=request.form['e_mail']
        user.adress=request.form['adress']
        user.adress_2=request.form['adress_2']
        db.session.commit()
        return redirect('/')
    return render_template('update.html',user=user) 

@app.route('/detail/<id>',methods=['GET','POST'])
def user(id):
    user=User.query.get(id)
    return render_template('detail.html',user=user)

db.create_all() 
if __name__ == '__main__':
    app.run(port=5000,debug=True)