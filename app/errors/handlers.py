from flask import render_template, Blueprint


errors = Blueprint('errors',__name__)


@errors.app_errorhandler(404)
def page_not_found(error):
    return render_template('error_page.html', err_title='Page you were looking for is not found.', err_desc='Please try again later or look elsewhere'), 404


@errors.app_errorhandler(403)
def access_denied(error):
    return render_template('error_page.html', err_title='Access to this specific URL is denied', err_desc='Please check your credentials and try again.'), 403


@errors.app_errorhandler(500)
def internal_error(error):
    return render_template('error_page.html', err_title='Internal error', err_desc='Please try again.'), 500

