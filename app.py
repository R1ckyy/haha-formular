from flask import Flask, request, render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators


app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
       return render_template()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run()
