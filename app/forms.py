from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Keyword(FlaskForm):
    """A form to gather a keyword.
    """
    keyword = StringField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Submit')
