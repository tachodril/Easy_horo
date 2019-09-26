from flask import Flask,jsonify
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(
    Developer='RITIK RAJ',
    Designation='employee at Tachodril'
    )

@app.route('/today/<sunsign>', methods=['GET'])
def daily(sunsign):
    my_url='http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/'+sunsign
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    container_for_date=page_soup.findAll("p",{"class":"orrange-text margin-bottom-0 margin-top-5 truncate-line"})
    return jsonify(result=containers[0].text.strip(),
                    date=container_for_date[0].text.strip(),
                    sunsign=sunsign
                    )

@app.route('/weekly/<sunsign>', methods=['GET'])
def weekly(sunsign):
    my_url='http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/'+sunsign
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    container_for_date=page_soup.findAll("p",{"class":"orrange-text margin-bottom-0 margin-top-5 truncate-line"})
    return jsonify(result=containers[0].text.strip(),
                    date=container_for_date[0].text.strip(),
                    sunsign=sunsign
                    )


@app.route('/monthly/<sunsign>', methods=['GET'])
def monthly(sunsign):
    my_url='http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/'+sunsign
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    container_for_date=page_soup.findAll("p",{"class":"orrange-text margin-bottom-0 margin-top-5 truncate-line"})
    return jsonify(result=containers[0].text.strip(),
                    date=container_for_date[0].text.strip(),
                    sunsign=sunsign
                    )


@app.route('/ritik', methods=['GET'])
def level():
    my_url='http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/aquarius'
    uclient=uReq(my_url)
    page_html=uclient.read()
    uclient.close()

    page_soup=soup(page_html,"html.parser")

    #containers2=page_soup.findAll("div",{"class":"row margin-bottom-0"})
    containers=page_soup.findAll("p",{"class":"margin-top-xs-0"})
    container_for_date=page_soup.findAll("p",{"class":"orrange-text margin-bottom-0 margin-top-5 truncate-line"})
    return jsonify(result=containers[0].text.strip(),
                    date=container_for_date[0].text.strip(),
                    sunsign=sunsign
                    )

if __name__ == '__main__':
    app.run()
