from flask import Flask
from extensions import db
from flask import request
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from time import sleep


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/consulta-cep')
def my_route():
    options = FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    #browser = Firefox()
    url = 'http://cep.republicavirtual.com.br/web_cep.php?cep='
    cep = request.args.get('cep')
    url = url + cep + '&formato=json'
    browser.get(url)
    browser_page_source = browser.page_source
    browser.quit() 
    return browser_page_source
  

app.run()