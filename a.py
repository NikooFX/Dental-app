from mailjet_rest import Client
import os

def send(mess=''):

    api_key = 'caa0ac8e4b590ab4ae288ae0790d8daf'
    api_secret = 'cc4859d060c08b1d020f5cfcc327eff4'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "sifarisvar@gmail.com",
                    "Name": "Saytdan Sifariş Var !!!"
                },
                "To": [
                    {
                        "Email": "denteca@mail.ru",
                        "Name": "Saytdan Sifariş Var !!!"
                    }
                ],
                "Subject": "Saytdan Sifariş Var !!!",
                "TextPart": "",
                "HTMLPart": mess,
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())