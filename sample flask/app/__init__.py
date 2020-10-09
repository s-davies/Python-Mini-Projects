from flask import (Flask, render_template, redirect)
# import config class
from app.config import Config
# import form class
from app.sample_form import SampleForm

app = Flask(__name__)
# populate Flask config dictionary from config class
app.config.from_object(Config)


@app.route('/')
def index():
    # keep sample simple with just a link to the form
    return '<h1>Simple App</h1><a href="/form">Form</a>'


@app.route('/form', methods=['GET', 'POST'])
def form():
    # instantiate form
    form = SampleForm()
    if form.validate_on_submit():
        return redirect('/')
    # send form into Jinja template (with form=form)
    return render_template('form.html', form=form)
