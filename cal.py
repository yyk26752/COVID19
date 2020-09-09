from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class Calendar(FlaskForm):
    month = SelectField(label="月", choices=list(range(1, 13)))
    day = SelectField(label="日", choices=list(range(1, 31)))
    submit = SubmitField(label="搜索")

