from flask import Flask,jsonify
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(
    {
    'Developer':'RITIK RAJ',
    'designation':'employee at Tachodril'
    }
    )

@app.route('/today/<sunsign>')
def daily(sunsign):
    my_url='http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/'+sunsign
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    return jsonify({'result':containers[0].text.strip()})

@app.route('/weekly/<sunsign>')
def weekly(sunsign):
    my_url='http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/'+sunsign
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    return jsonify({'result':containers[0].text.strip()})


@app.route('/monthly/<sunsign>')
def monthly(sunsign):
    my_url='http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/'+sunsign
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    return jsonify({'result':containers[0].text.strip()})


@app.route('/ritik')
def level():
    my_url='http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/aquarius'
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    return containers[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
