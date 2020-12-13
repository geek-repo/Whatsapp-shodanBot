from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from shodanfetch import sh


app = Flask(__name__)

@app.route("/")

def help():
    return "*Welcome to Shodan API*"


@app.route("/sms", methods=['POST'])

def sms_reply():
    msg = request.form.get('Body')
    resp = MessagingResponse()
    if msg=="help" or msg=="Help" or msg=="HELP":
        resp.message(helpbanner())
        return str(resp)
    else:
        return str(sh(msg,resp))

def helpbanner():
    return "*Welcome to Shodan API* \nQuery syntax\nhost:8.8.8.8\nport:445\norg:Amazon\nport:445 org:Amazon country:IN\n *LEVELS OF RESULTS* \n --level 1 :- 10 records max\n--level 2 :- 5 pages of results\n--level 3 :- top 50 pages of results\n\n *FINAL QUERY* \nport:445 org:Amazon country:IN --level 3\n\n_Note:- IF NO LEVEL IS PASSED Default level is set to 1_\n\n*Made By Sarthak*"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
