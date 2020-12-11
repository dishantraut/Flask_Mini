# from wtforms import SubmitField, BooleanField, StringField,PasswordField, validators
# from flask_wtf import FlaskForm
from flask import Flask, request, render_template
from model import RegForm
from flask_bootstrap import Bootstrap
#
# class RegForm(FlaskForm):
#   name_first = StringField('First Name',[validators.DataRequired()])
#   name_last = StringField('Last Name',[validators.DataRequired()])
#   email = StringField('Email Address', [validators.DataRequired(),validators.Email(), validators.Length(min=6, max=35)])
#   password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm',message='Passwords must match')])
#   confirm = PasswordField('Repeat Password')
#   submit = SubmitField('Submit')


app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)
@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return '<h2>We confirm your registration!</h2>'
    return render_template('registration.html', form=form)
if __name__ == '__main__':
    app.run()
