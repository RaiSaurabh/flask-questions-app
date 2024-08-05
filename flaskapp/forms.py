from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField


class QuestionForm(FlaskForm):
    """Represents a new test suite form

    This class represents a new test suite form. It uses flask-wtf form fields
    and validators to construct the form and validate input.

    """
    summary = StringField(u'Question summary')
    question = TextAreaField(u'Question')
