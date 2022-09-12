from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = StringField('Author', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Create')


class UpdateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = StringField('Author', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Update')


class DeleteBookForm(FlaskForm):
    submit = SubmitField('Delete')

