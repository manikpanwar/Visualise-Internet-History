Visualise-Internet-History
==========================
This is a python application which helps users visualise their Google Chrome web browsing history in the form of a graph network built according to pages visited. This uses JSON to parse the web history and the Ubigraph library. 

Set Up:

1. Get the Chrome extension Export History and save your history as a JSON file in your development folder. Name it as 'history.json'
2. Download  and save in development folder. ubigraph : http://ubietylab.net/ubigraph/content/Downloads/index.php
3. Setup ubigraph and start a ubigraph server according to instructions on file. Do that by locating the ubigraph folder in terminal and going /bin/ubigraph_server
4. Ubigraph server can also be run by looking up where it is located in the development folder and setting   ubiGraph_server variable in executeServer.py as that and running it.
5. Run pyNetworkUbi.py

