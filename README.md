# Easy_horo
<h1>Horoscope API and application</h1>

An API to extract horoscope using web scraping.

<h2>Features :</h2>

<li>Today's horoscope</li>
	    Jsonified into date, horoscope and sunsign.
<li>Weekly horoscope</li>
	    Jsonified into week, horoscope and sunsign.
<li>Monthly horoscope</li>
	    Jsonified into month, horoscope and sunsign.

<h2>API Usage :</h2>

<h4>Usage 1.</h4> Web Page Link that uses the API : https://easyhoro.herokuapp.com/

<h6>Steps included:</h6>

1. Open the above link in your browser. 
2. Now, select your sunsign and time for which you want to know your horoscope.
3. Click on ‘submit’ button.
4. There you go. (To get another horoscope, follow steps 2 & 3 again.)

<h4>Usage 2.</h4> You can directly open the api server and use json data in your app.

API Base URL : https://easy-horo.herokuapp.com/

GET : <b> /today/sunsign </b><br>
GET : <b> /weekly/sunsign </b><br>
GET : <b> /monthly/sunsign </b><br>

Example Usage 2: GET https://easy-horo.herokuapp.com/today/aquarius

Example Result:
			
			{
        "date":"27-09-2019",
        "result":"You will seek spirituality as you feel thoroughly dejected by your present situation.
                Ritik says that even struggling courageously with circumstances requires a spiritual endeavour. 
                These trying times give you the patience to deal intelligently with challenges and setbacks.",
        "sunsign":"aquarius"
      }


<h2>Development:</h2>

<li>Web Scraping from a horoscope website (ganeshaspeaks) using Python and Beautiful Soup.</li>
<li>Using Flask, created server and RESTful API to return requested JSON data.</li>
<li>Created a web page to show example of using the above created API and used javascript to fetch API and parse JSON data.</li>
<li>Used Heroku cloud platform to host the API server as well as web page.</li>

<h2>Tools Used :</h2>

<li>Beautiful Soup </li>
<li>Flask </li>
<li>Requests (Pyhton Module) </li>
<li>Heroku (cloud platform) </li>
