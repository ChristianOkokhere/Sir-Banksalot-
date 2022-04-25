import setup
from setup import SendMessage
from Time import gettime
#this is what will send messages when called based on params passed to the function
def sendy(type):
    to = "cokokhere@gmail.com"
    sender = "cokokhere@gmail.com"

    msgPlain = "Hi\nPlain Email"
    if type == "investment":
        subject = "MONTHLY INVESTMENT"
        msgHtml = "This is you monthly investment email, this month you have ___ to invest <br/>"
    if type == "pay":
        subject = "WEEKLY PAY"
        msgHtml = "This is you payment email, this period you have ___ to spend <br/>"
    SendMessage(sender, to, subject, msgHtml, msgPlain)


    
if __name__ == '__main__':
    sendy("pay")
