// importing the request library 
 request = require('request-promise')

//api endpoint prefix 
const URLprefix = 'https://api.thingspeak.com/update?api_key=<YOUR_THINGSPEAK_CHANNEL_KEY>&field1='

// sending GET request and Callback function for response
const URL= URLprefix+Math.floor(Math.random() * 11)

request(URL)
.then(response => 
    console.log(response) // print output to console
)
.catch(error => console.log(error));



