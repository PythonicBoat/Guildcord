from functools import wraps
from flask import request, redirect, url_for, session, flash
import random
import string

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first.')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def random_str(no=6):
    answer = ""
    for i in range(no):
        answer += random.choice(string.ascii_letters + string.digits)

def timestamp():
    from datetime import datetime
    datetimeobj = datetime.now()
    timestamp = datetimeobj.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp