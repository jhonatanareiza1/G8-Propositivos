# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:37:26 2022

@author: USER
"""

from flask import Flask
import os
from twilio.rest import Client

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from flask import request

app = Flask(__name__)


@app.route("/")
def inicio():
    test = os.environ.get('test')
    return test

@app.route("/sms")
def sms():
    try:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        contenido = request.args.get("mensaje")
        destino = request.args.get("telefono")
        message = client.messages \
                    .create(
                         body = contenido,
                         from_='+19853046799',
                         to = '+57' + destino
                     )
    
        print(message.sid)
        return "eniviado full bn"
    except Exception as e:
        return "Error enviando el msn"
    
@app.route("/envio-correo")
def email():
    
        destino = request.args.get("correo_destino")
        asunto = request.args.get("asunto")
        mensaje = request.args.get("contenido")    
    
        message = Mail(
            from_email='jhonatanareiza1@hotmail.com',
            to_emails = destino,
            subject = asunto,
            html_content = mensaje)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return "correo Enviado al pelo"
        except Exception as e:
            print(e.message)
            return "error de envio de correo"

if __name__ == '__main__':
    app.run()