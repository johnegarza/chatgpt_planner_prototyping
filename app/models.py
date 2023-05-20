from datetime import datetime
from . import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    notes = db.relationship('NoteTag', back_populates='tag', secondary='notes_tags')
    tasks = db.relationship('TaskTag', back_populates='tag', secondary='tasks_tags')

class NoteTag(db.Model):
    __tablename__ = 'notes_tags'
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False, primary_key=True)

class TaskTag(db.Model):
    __tablename__ = 'tasks_tags'
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False, primary_key=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = db.relationship('Tag', secondary='notes_tags', backref=db.backref('notes', lazy='dynamic'))
    project = db.Column(db.String(120))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    priority = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.relationship('Note', backref='task', lazy=True)
    tags = db.relationship('Tag', secondary='tasks_tags', backref=db.backref('tasks', lazy='dynamic'))
    project = db.Column(db.String(120))

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

