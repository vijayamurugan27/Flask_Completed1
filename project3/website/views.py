from flask import Blueprint, render_template, flash, request, jsonify, json
from flask_login import login_required,  current_user
from .models import Note
from .import db

views = Blueprint('views', __name__)


@views.route('/')
@views.route('index')
@login_required
def home():
    return render_template("app/home.html", name = 'Kavin', age= '45', user = current_user)


@views.route('service')
def service():
    return render_template("app/service.html", user = current_user)


@views.route('product')
def product():
    return render_template("app/product.html", user = current_user)

@views.route('about')
def about():
    flash('This is a flash error message', 'error')
    flash('This is a flash Sucess message', 'Success')
    return render_template('app/about.html', user = current_user)


@views.route('notes',methods = ['GET', 'POST'])
def note():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Note is too short", category = 'error')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("note is added", category = 'success')


    return render_template('app/note.html', user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)    
    print(current_user.id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

