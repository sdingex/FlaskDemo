from flask import render_template, flash, redirect, session, url_for, request
from FlaskDemo import app, db


@app.route('/st')
def st_index():
    return render_template('/st/st.htm')