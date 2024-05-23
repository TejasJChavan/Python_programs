from selenium import webdriver
import bs4, smtplib, requests
from selenium.webdriver.chrome.options import Options
from email.message import EmailMessage
from googletrans import Translator

chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.motilaloswal.com/markets/stock-market-live/movi.aspx')
gold_code = browser.execute_script("return document.documentElement.outerHTML")
gold_important = bs4.BeautifulSoup(gold_code, 'html5lib')
browser.quit()

browser = webdriver.Chrome()
browser.get('https://www.policybazaar.com/silver-rate/')
silver_code = browser.execute_script("return document.documentElement.outerHTML")
silver_important = bs4.BeautifulSoup(silver_code, 'html5lib')
browser.quit()


def gold_value():
    whole_thing = gold_important.select('#lblGoldData')
    value = (whole_thing[0].getText())
    return value


def silver_value():
    whole_thing = silver_important.select('.dailyGoldrate')
    only_value = whole_thing[0].getText()
    value = f'चांदी : {only_value}'
    return value



senders_email_address = 'forusebypythononly@gmail.com'
app_psswd = 'azxgknicehgcomdz'


translator = Translator()
to_be_translated = f'{gold_value()}'
to_be_sent = translator.translate(to_be_translated, dest='mr').text

greeting = "This is your today's information :"
mar_greeting = translator.translate(greeting, dest='mr').text


msg = EmailMessage()
msg['Subject'] = f'{to_be_sent} || {silver_value()}'
msg['From'] = senders_email_address
msg['To'] = ['sweetchilly321@gmail.com', 'sapnajchavan@gmail.com']
msg.set_content(f'{to_be_sent}, {silver_value()}')
msg.add_alternative('''\
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>BOOM</title>
  <style>
    .mainbox {
      background-color: #F1F0CD;
      text-align: center;
      height: 300px;
      width:50%;
      border: solid 10px;
      border-radius: 10%;
      padding: 20px;
      border-color: #CAC99B;
      font-family: Arial;
      margin-left: auto;
      margin-right: auto;
    }

    .greeting {
      text-align: center;
    }

    .everything {
      text-align: center;
    }
    .mainbox:hover{
      border-radius: 10%;
    }
  </style>

</head>

<body>
  <div class="mainbox">
    <br>
    <br>
    <h1 class="greeting">''' + mar_greeting + '''</h1>
      <p class="everything">
        '''+to_be_sent+'''<br>
        <br>
        <br>
        '''+silver_value()+'''
      </p>
  </div>
</body>

</html>
''', subtype='html')


smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.login(senders_email_address, app_psswd)
smtpObj.send_message(msg)
smtpObj.quit()
