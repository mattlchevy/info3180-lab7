from flask_wtf import FlaskForm
from flask import Flask
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from flask_wtf.file import FileRequired, FileField, FileAllowed


class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'bmp', 'png'], 'Images only!')])
