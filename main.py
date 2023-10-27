from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

@app.route('/')
def main():
    lista = Item.query.all()
    db.create_all()
    return render_template('index.html', lista=lista)

@app.route('/new', methods=['POST', 'GET'])
def add_task():
    if request.method == 'POST':
        task = Item(task=request.form['task_name'], checked=False)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main'))
    else:
        return render_template('index.html', create=True)
    
@app.route('/<int:task_id>/edit', methods=['POST', 'GET'])
def edit(task_id):
    if request.method == 'POST':
        task = Item.query.get(task_id)
        task.task = request.form['task_name']
        db.session.commit()
        return redirect(url_for('main'))
    else:
        task = Item.query.get(task_id)
        return render_template('index.html', create=True, edit=True, task=task.task)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Item.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main'))

@app.route('/check/<int:task_id>')
def check(task_id):
    task = Item.query.get(task_id)
    task.checked = not task.checked
    db.session.commit()
    return redirect(url_for('main'))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    checked = db.Column(db.Boolean)
    
if __name__ == "_main__":
    app.run(debug=False, host='0.0.0.0')