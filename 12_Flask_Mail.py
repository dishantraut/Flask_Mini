  
""" https://pythonhosted.org/Flask-Mail/ """
# importing libraries
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER']='karmamgmt.icewarpcloud.in'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'empeng@karmamgmt.com'
app.config['MAIL_PASSWORD'] = 'i@mgoingtobeMultiplebusinessholder25'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message('Hello', sender = 'empeng@karmamgmt.com' )

    msg.recipients = ['dishantraut@gmail.com']
    msg.subject = 'Flask Mail Testing'
    msg.cc = ['dishant@karmamgmt.com']
    msg.bcc = ['']
    # msg.attachments  = [r'D:\Python_VE\try_VE1\flask_demo\REST\test.py']
    msg.body = """
    Dear Dishant,
    Please IGNORE THE LAST RECEIVED MAIL IT WAS FOR TESTING PURPOSE.
    IF YOU FIND ANY ERRORS IN TICKET NOMENCLATURE / DID NOT RECEIVE THE TICKET.
    PLEASE MAIL ME AT 'dishant@karmamgmt.com'
    THIS IS YOUR FINAL TICKET FOR BINGO GAME.
    Please find attached your LUCKY TICKET for BINGO !!
    YOU CAN WIN IN THE FOLLOWING CATEGORIES :-
    Early Five    :  The ticket with first five number striked out.
    Top Line      :  The ticket with all the numbers of the top row striked out fastest.
    Middle Line   :  The ticket with all the numbers of the middle row striked out fastest.
    Bottom Line   :  The ticket with the numbers of the bottom row striked out fasted.
    Four Corners  :  The ticket with all four corners striked out first i.e. 1 st and last numbers of top and bottom rows.
    Full House    :  The ticket with all the numbers striked out first.
    Wish You All The Very Best
    [  This Is An Auto Generated E-mail - Please Do Not Reply  ]
    """

    mail.send(msg)
    return "<h1>Sent</h1>"

if __name__ == '__main__':
   app.run(debug = True)
