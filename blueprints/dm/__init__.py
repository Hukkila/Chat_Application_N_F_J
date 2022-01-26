from flask import Blueprint, render_template, redirect, url_for, request

from controllers.user_controller import get_all_users

bp_dm = Blueprint('bp_dm', __name__)


@bp_dm.get('/dm')
def dm_get():
    users = get_all_users()
    return render_template('dm.html', users=users)
