from flask import render_template, redirect, url_for, request
from pytodo.extensions.database import db
from pytodo.extensions.model import Item

def init_app(app):
    @app.route('/')
    def main():
        db.create_all()
        lista = Item.query.all()
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