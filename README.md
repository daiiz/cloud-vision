# Google Cloud Vision API Client
This is a tool to try the feature `LABEL_DETECTION` of Google Cloud Vision API.
[![https://gyazo.com/0aa5cddd30b8bbc956aa6ced95fd244c](https://i.gyazo.com/0aa5cddd30b8bbc956aa6ced95fd244c.png)](https://gyazo.com/0aa5cddd30b8bbc956aa6ced95fd244c)

## Set your API key
```
$ echo "CLOUD_VISION='YOUR_API_SERVER_KEY'\n" >> googleapikeys.py
```

## Install pip modules
```
$ pip install -r pip_modules.txt
```

## Install tfPhotoPalette
You can get it in Chrome Web Store:
https://chrome.google.com/webstore/detail/tfphotopalette/gcpfanfkkjpolcdicokfjphmdnelhbbb

## Run local server
```
$ python palette_server.py
```

## Run tfPhotoPalette and Send requests
Give your favorite photo. You can give a photo in following two ways.
* Drag and drop a photo file onto tfPhotoPalette app.
* Enter the URL of a photo in the Web and click "Load" button.

[![https://gyazo.com/1484dd1d17d3261f550b695f2e8d3a2f](https://i.gyazo.com/1484dd1d17d3261f550b695f2e8d3a2f.gif)](https://gyazo.com/1484dd1d17d3261f550b695f2e8d3a2f)

And then, click "Play" button in right-bottom of the window.
The small window for sending request to local server will open.
Select the value `Original photo` in a left-top select button.
In the last step, click "Classify" button to send `LABEL_DETECTION` request to Google Cloud Vision API through the local server you launched before.

## Get response
You can get `labelAnnotations` results.
[![https://gyazo.com/14f57b3eee0b2f636251a5e9f089984d](https://i.gyazo.com/14f57b3eee0b2f636251a5e9f089984d.png)](https://gyazo.com/14f57b3eee0b2f636251a5e9f089984d)


Please go to http://daiiz.hatenablog.com/entry/2016/03/26/020347 for more details.
