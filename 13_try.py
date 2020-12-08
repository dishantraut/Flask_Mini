from flask import Flask, render_template, request, flash
from forms_13 import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()

   if request.method == 'POST':
      if form.validate() == False:
         # flash('All fields are required.')
         flash('Data Missing')
         return render_template('13_contact.html', form = form)
      else:
         return "<h1>Form Posted Successfully</h1>"
   elif request.method == 'GET':
      return render_template('13_contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)
