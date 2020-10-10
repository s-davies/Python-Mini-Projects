from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import (DataRequired, ValidationError)
from wtforms.widgets.html5 import (DateInput, TimeInput)
from datetime import datetime


class AppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[
                           DataRequired()], widget=DateInput())
    start_time = TimeField("Start Time", validators=[
                           DataRequired()], widget=TimeInput())
    end_date = DateField("End Date", validators=[
                         DataRequired()], widget=DateInput())
    end_time = TimeField("End Time", validators=[
                         DataRequired()], widget=TimeInput())
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private?")
    submit = SubmitField("Create an Appointment")

    def validate_end_date(form, field):
        start = form.start_date.data
        end = field.data
        if start != end:
            msg = "End date must be the same as start date"
            raise ValidationError(msg)
