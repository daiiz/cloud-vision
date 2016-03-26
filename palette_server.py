# coding: utf-8
from flask import Flask, request, jsonify
import urllib
import base64
import json
import requests
import googleapikeys

app = Flask(__name__)
default_port = 52892

GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

def goog_cloud_vison (image_content):
    api_url = GOOGLE_CLOUD_VISION_API_URL + googleapikeys.CLOUD_VISION
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_content
            },
            'features': [{
                'type': 'LABEL_DETECTION',
                'maxResults': 10,
            }]
        }]
    })

    res = requests.post(api_url, data=req_body)
    return res.json()


@app.route('/', methods=['GET'])
def hello ():
    return 'Hello! This is palette_server.'


@app.route('/api/classify', methods=['POST'])
def classify ():
    # tfPhotoPaletteから受信するJSON形式のリクエスト
    tfpp_json = request.json
    if ('jpg' in tfpp_json):
        image_base64_str = tfpp_json['jpg'].replace('data:image/jpeg;base64,', '')
        img_jpg = image_base64_str.decode('base64')
        image_content = base64.b64encode(img_jpg)
        # Label Detection: Google Cloud Vision で物体認識する
        res_json = goog_cloud_vison(image_content)

        # tfPhotoPalette向けの付加情報
        res_json['description'] = 'Label Detection (Google Cloud Vision)'

        return jsonify(res_json)
    else:
        return jsonify(description='Bad request')

app.run(port=default_port)
