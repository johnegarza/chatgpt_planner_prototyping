from flask import Blueprint, request, render_template, redirect, url_for
from datetime import datetime
from .models import Note, Tag
from . import db

views = Blueprint('views', __name__)

@views.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        tags = request.form['tags']
        project = request.form['project']

        new_note = Note(title=title, body=body, tags=tags, project=project)
        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('views.notes'))

    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('notes.html', notes=notes)

@views.route('/notes/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)

    if request.method == 'POST':
        note.title = request.form['title']
        note.body = request.form['body']
        note.tags = request.form['tags']
        note.project = request.form['project']
        note.last_modified = datetime.now()
        db.session.commit()

        return redirect(url_for('views.notes'))

    return render_template('edit_note.html', note=note)

@views.route('/new_note', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        tag_names = request.form['tags'].split(',')
        project = request.form['project']

        tags = []
        for tag_name in tag_names:
            tag_name = tag_name.strip()  # Remove leading/trailing whitespace
            tag = Tag.query.filter_by(name=tag_name).first()
            if tag is None:
                tag = Tag(name=tag_name)
                db.session.add(tag)

            tags.append(tag)

        new_note = Note(title=title, body=body, tags=tags, project=project)

        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('views.notes'))

    return render_template('new_note.html')
