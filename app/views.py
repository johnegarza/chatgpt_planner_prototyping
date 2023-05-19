from flask import request, render_template, redirect, url_for
from datetime import datetime
from . import db, app
from .models import Note

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        tags = request.form['tags']
        project = request.form['project']

        new_note = Note(title=title, body=body, tags=tags, project=project)
        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('notes'))

    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('notes.html', notes=notes)

@app.route('/notes/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)

    if request.method == 'POST':
        note.title = request.form['title']
        note.body = request.form['body']
        note.tags = request.form['tags']
        note.project = request.form['project']
        note.last_modified = datetime.now()
        db.session.commit()

        return redirect(url_for('notes'))

    return render_template('edit_note.html', note=note)

