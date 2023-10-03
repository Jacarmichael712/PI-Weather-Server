PI WEATHER SERVER BY JAMES CARMICHAEL

This project uses a Raspberry PI 3 B+ to create a server that will get API
info from WeatherAPI.com and show you the weather forecast in your area.

You will need to make a config.py file to include your own personal
API key if you wish to use this code on your own PI

The server will passively wait for a socket connection from a client.
The client will connect to the server and request the weather information.
The server will get weather information from the API and return
the results to the client and proceed to end the connection.

This project makes use of:
 - Server-client network architecture using IPv4 sockets
 - API requests
