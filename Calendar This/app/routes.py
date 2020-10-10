from flask import (Blueprint, render_template, redirect, url_for)
from app.forms import AppointmentForm
from datetime import (datetime, timedelta)
import os
import psycopg2


bp = Blueprint('main', __name__, url_prefix='')
CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}


@bp.route("/")
def main():
    d = datetime.now()
    return redirect(url_for(".daily", year=d.year, month=d.month, day=d.day))
    # return redirect(f'/{d.year}/{d.month}/{d.day}')


@bp.route("/<year>/<month>/<day>", methods=['GET', 'POST'])
def daily(year,month,day):
    form = AppointmentForm()
    d = datetime(int(year),int(month),int(day))
    nd = d + timedelta(1)
    if form.validate_on_submit():
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
            'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
            'description': form.description.data,
            'private': form.private.data
        }
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute("""
                            INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
                            VALUES (%(name)s, %(start_datetime)s,
                            %(end_datetime)s, %(description)s, %(private)s)
                            """,
                             params)
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                        SELECT id, name, start_datetime, end_datetime
                        FROM appointments
                        WHERE start_datetime BETWEEN %(day)s AND %(next_day)s
                        ORDER BY start_datetime
                        """,
                        {
                            "day": d,
                            "next_day": nd
                        })
            rows = curs.fetchall()
            return render_template("main.html", rows=rows, form=form)
