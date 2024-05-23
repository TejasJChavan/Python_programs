from selenium import webdriver
import bs4, smtplib, requests, os, imghdr
from selenium.webdriver.chrome.options import Options
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

try :
    # range_request = requests.get('http://www.motilaloswalmf.com/CMS/images/Content_Images/image-21101887761st%20image.png')
    # f = open('range.png', 'wb+')
    # f.write(range_request.content)
    # f.close()
    #
    # f = open('range.png', 'rb')
    # file_data = f.read()
    # file_type = imghdr.what(f.name)
    # file_name = f.name
    #
    # value_request = requests.get('http://www.motilaloswalmf.com/CMS/images/Content_Images/image18582271302nd%20image.png')
    # fv = open('value.png', 'wb+')
    # fv.write(value_request.content)
    # fv.close()
    #
    # fv = open('value.png', 'rb')
    # vfile_data = fv.read()
    # vfile_type = imghdr.what(fv.name)
    # vfile_name = fv.name

    f = open('range.png', 'rb')
    ranges = f.read()
    rtype = imghdr.what(f.name)
    rname = f.name
    f.close()

    f = open('value.png', 'rb')
    value = f.read()
    vtype = imghdr.what(f.name)
    vname = f.name
    f.close()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.motilaloswal.com/markets/stock-market-live/movi.aspx')
    code = browser.execute_script("return document.documentElement.outerHTML")
    browser.quit()
    important = bs4.BeautifulSoup(code, 'html5lib')


    def search(value):
        pattern = re.compile('\d*(,)?\d*\.\d*')
        partial = pattern.search(value)
        lesspartial = partial.group()
        good = lesspartial.replace(',', '')
        return good


    def date_value():
        whole_thing = important.select('#lblMOVIDate')
        date = (whole_thing[0].getText())
        return date


    def nifty_value():
        whole_thing = important.select('#lblNiftyData')
        value = (whole_thing[0].getText())
        return value


    def sensex_value():
        whole_thing = important.select('#lblSensexData')
        value = (whole_thing[0].getText())
        return value


    def usdinr_value():
        whole_thing = important.select('#lblUsrData')
        value = (whole_thing[0].getText())
        return value


    def movi_subject_value():
        whole_thing = important.select('#lblMOVIVal')
        value = (whole_thing[0].getText())
        actual = f'MOVI: {value}'
        return actual


    def movi_body_value():
        whole_thing = important.select('#lblMOVIVal')
        value = (whole_thing[0].getText())
        if float(value) < 90:
            actual = f'''MOVI: {value}

                Seems like a good time to invest !'''
            return actual
        elif float(value) > 110:
            actual = f'''MOVI: {value}

                No, I don't think you should invest.'''
            return actual
        else:
            actual = f'''MOVI: {value}

                Nothing Interesting.'''
            return actual


    def gold_value():
        whole_thing = important.select('#lblGoldData')
        value = (whole_thing[0].getText())
        return value


    def do_the_main_thing():
        money_list = [nifty_value(), sensex_value(), usdinr_value(), gold_value(), movi_body_value()]
        print(f'For {date_value()}:')
        for item in money_list:
            print(item)


    only_nifty = search(nifty_value())
    only_sensex = search(sensex_value())
    only_usdinr = search(usdinr_value())
    only_gold = search(gold_value())
    only_movi = search(movi_subject_value())

    fd = open('date.txt', 'r')
    prev_date = fd.read()
    fd.close()
    if str(prev_date) != str(date_value()):
        fdw = open('date.txt', 'w')
        fdw.write(date_value())
        fdw.close()
        scope = ['https://www.googleapis.com/auth/drive']

        cred = ServiceAccountCredentials.from_json_keyfile_name('BabaAnandiAahe-28acda00c3a6.json', scope)

        client = gspread.authorize(cred)

        sheet = client.open('BabaAnandiAahe').sheet1

        stuff = [date_value(), float(only_nifty), float(only_sensex), float(only_usdinr), float(only_gold),
                 float(only_movi)]

        sheet.insert_row(stuff, 2)

    link = 'https://docs.google.com/spreadsheets/d/1_InKvaq9SNg7skNiE9JdpXEalaAUrcgJKtuyU9VcV6E/edit?usp=sharing'
    sitelink = 'https://www.motilaloswal.com/markets/stock-market-live/movi.aspx'

    do_the_main_thing()

    senders_email_address = 'forusebypythononly@gmail.com'
    app_psswd = 'azxgknicehgcomdz'

    msg = EmailMessage()
    msg['Subject'] = f'{nifty_value()} | {sensex_value()} | {usdinr_value()} | {gold_value()} | {movi_subject_value()}'
    msg['From'] = senders_email_address
    msg['To'] = ['sweetchilly321@gmail.com', 'jagdishc.inf@gmail.com']
    msg.set_content('This is plain')
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
          height: 500px;
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
        <h1 class="greeting">Here you go with today's data :</h1>
          <p class="everything">
            ''' + nifty_value() + '''<br>
            <br>
            ''' + sensex_value() + '''<br>
            <br>
            ''' + usdinr_value() + '''<br>
            <br>
            ''' + gold_value() + '''<br>
            <br>
            ''' + movi_body_value() + '''<br>
            <br>
            <br>
            <a href="https://www.motilaloswal.com/markets/stock-market-live/movi.aspx">Motilal Oswal</a><br>
            <br>
            <a href="https://docs.google.com/spreadsheets/d/1_InKvaq9SNg7skNiE9JdpXEalaAUrcgJKtuyU9VcV6E/edit?usp=sharing">Google Document</a>
          </p>
      </div>
    </body>

    </html>
    ''', subtype='html')
    msg.add_attachment(ranges, maintype='image', subtype=rtype, filename=rname)
    msg.add_attachment(value, maintype='image', subtype=vtype, filename=vname)

    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login(senders_email_address, app_psswd)
    smtpObj.send_message(msg)
    smtpObj.quit()

    # os.remove('value.png')
    # os.remove('range.png')

except Exception as e:
    senders_email_address = 'forusebypythononly@gmail.com'
    app_psswd = 'azxgknicehgcomdz'

    msg = EmailMessage()
    msg['Subject'] = f'Oops! Something went wrong!'
    msg['From'] = senders_email_address
    msg['To'] = ['sweetchilly321@gmail.com']
    msg.set_content(f'''The following error message has occured: {e} 

Please contact sweetchilly321@gmail.com for any further concern

''')

    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login(senders_email_address, app_psswd)
    smtpObj.send_message(msg)
    smtpObj.quit()

    print(e)
