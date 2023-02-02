from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError
from random import randrange

SECRET_KEY = 'fuckoffbiatch'

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/week1', methods=["GET", "POST"])
def week1():
    class CorrectAnswer(object):
        def __init__(self, answer):
            self.answer = answer

        def __call__(self, form, field):
            message = "Incorrect Answer."
            if field.data != self.answer:
                raise ValidationError(message)

    class Quiz(Form):
        class Meta:
            csrf = False

        q1 = RadioField("What is a black box test",
                        choices=[
                            ('A', 'Some made up term'),
                            ('B', 'A test with no knowledge provided to the testing team'),
                            ('C', 'A test with minimal knowledge provided to the team'),
                            ('D', 'An illegal test performed without permission')
                        ],
                        validators=[CorrectAnswer('B')])
        q2 = RadioField("Why would a company prefer a white box test instead of a black box test",
                        choices=[
                            ('A', 'A white box test provides the closest to a legitimate attack'),
                            ('B', 'To ensure a wider coverage of the systems being tested'),
                            ('C', 'There is no such thing as white box and black box testing'),
                            ('D', 'None of the above')
                        ],
                        validators=[CorrectAnswer('B')])
        q3 = RadioField("What are the five phases of penetration testing?",
                        choices=[
                            ('A',
                             "Information Gathering, Enumeration/Scanning, Exploitation, Privilege Escalation, Post-Exploitation"),
                            ('B', 'Recon, Scanning, Exploitation, Lateral Movement, Reporting'),
                            ('C',
                             'Vulnerability Scanning, Exploitation, Information Gathering, Lateral Movement, Reporting'),
                            ('D', 'Information Gathering, Exploitation, Privilege Escalation, Clean up, Reporting ')],
                        validators=[CorrectAnswer('A')])
        q4 = RadioField("What phase of the pentesting methodology does reporting fall under?",
                        choices=[('A', "Information Gathering"),
                                 ('B', "Exploitation"),
                                 ('C', "Clean Up"),
                                 ('D', 'Post-Exploitation')],
                        validators=[CorrectAnswer('D')]
                        )
        q5 = RadioField("When walking a web application, what is one of the first things you should check. When you "
                        "do that, there is something that you should always look for, sometimes breadcrumbs can be "
                        "left by devs. Find the bread crumb to answer this question.",
                        choices=[
                            ('A', 'A'),
                            ('B', 'B'),
                            ('C', 'C'),
                            ('D', 'D')],
                        validators=[CorrectAnswer('C')]
                        )
        q6 = RadioField("You are performing a NMAP scan on a host, and the host comes back as 'host down'. What flag "
                        "should you use, if any, to verify the host is actually down?",
                        choices=[('A', '-sV'),
                                 ('B', '-Pn'),
                                 ('C', '-pn'),
                                 ('D', 'None, if the host is down move on to the next host')
                                 ],
                        validators=[CorrectAnswer('B')]
                        )
        q7 = RadioField("Regarding the last question, what protocol may be blocked if you are receiving a host down "
                        "that is actually up?",
                        choices=[
                            ('A', "Internet Control Message Protocol"),
                            ('B', 'Secure Socket Shell'),
                            ('C', 'HyperText Transfer Protocol'),
                            ('D', 'None of the above')
                        ],
                        validators=[CorrectAnswer('A')]
                        )
        q8 = RadioField("You need to use the NSE script ssl-enum-ciphers. Your base nmap scan is nmap -iL hosts.txt "
                        "-sV. What do you need to add to run the script.",
                        choices=[
                            ('A', '-s ssl-enum-ciphers'),
                            ('B', '--script ssl*'),
                            ('C', '-script=ssl-enum-ciphers'),
                            ('D', '--script=ssl-enum-ciphers')
                        ],
                        validators=[CorrectAnswer('D')])
        q9 = RadioField("What flag can you use to save the output of nmap in greppable format?",
                        choices=[
                            ('A', '-oN'),
                            ('B', '-ON'),
                            ('C', '-Og'),
                            ('D', '-oG')
                        ],
                        validators=[CorrectAnswer('D')])
        q10 = RadioField("You are testing an application, and you notice that you can replace a number in the URL to access data you should not be able to see. What vulnerability are you most likely looking at?",
                         choices=[
                             ('A', "Insecure Direct Object Referencing"),
                             ('B', 'Structured Query Language Injection'),
                             ('C', 'Cross Site Scripting'),
                             ('D', 'ServerSide Request Forgery')
                         ],
                         validators=[CorrectAnswer('A')]
                         )

    form = Quiz()
    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('week1.html', quiz=form)


if __name__ == '__main__':
    app.run(debug=True)
