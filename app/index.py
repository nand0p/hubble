from flask import Flask
import requests
import random


image_count = 4670
api_endpoint = 'https://hubblesite.org/api/v3/image/'

app = Flask(__name__)


@app.route('/')
def home():
    html = get_header()
    html += get_image()
    html += get_footer()
    return html


def get_footer():
    return '<p>This site refreshes every 20 seconds with a new image from the NASA Hubble Telescope archives' + \
           '<p>Source Code: <a href=https://github.com/nand0p/hubble>https://github.com/nand0p/hubble</a>' + \
           '<p>If you find this useful, please contribute:<br><b>' + \
           'BTC: 112JJvxsvRYn4QtpWJqZmLsTbPEG7aPsdB<br>' + \
           'ETH: 0x5b857cc1103c82384457BACdcd6E2a9FCD0b7e2A</b>' + \
           '<p>SEDME</font></body></html>'

def get_header():
    return '<html><head><title>NASA Image SlideShow</title><meta http-equiv=refresh content=20>' + \
           '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-32710227-3"></script>' + \
           '<script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} ' + \
           'gtag("js", new Date()); gtag("config", "UA-32710227-3"); </script>' + \
           '<script data-ad-client="ca-pub-9811914588681081" async ' + \
           'src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>' + \
           '</head><body bgcolor="black"><font color="white">'

def get_image():    
    image_num = str(random.randint(1, image_count))
    rez = requests.get(api_endpoint + image_num).json()
    if rez.get('image_files'):
        image_url = rez['image_files'][-1]['file_url']
        if image_url.endswith('tif') or image_url.endswith('tiff') or image_url.endswith('pdf') or image_url.endswith('epub'):
            if len(rez['image_files']) > 1:
                image_url = rez['image_files'][-2]['file_url']
            else:
                image_url = '//imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/29288/STScI-H-spacecraft24-3072x2040.jpg'
            if image_url.endswith('tif') or image_url.endswith('tiff') or image_url.endswith('pdf') or image_url.endswith('epub'):
                image_url = '//imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/29288/STScI-H-spacecraft24-3072x2040.jpg'
    else:
        image_url = '//imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/29288/STScI-H-spacecraft24-3072x2040.jpg'
    if rez.get('name'):
        image_name = rez['name']
    else:
        image_name = 'unnamed'
    _html = str(image_num) + ' ' + image_name + '<br>'
    _html += '<img src=https:' + image_url + ' height=95%><br>' + image_url + '<p>'
    if rez.get('description'):
        _html += rez['description']
    _html += '<p>'
    if rez.get('credits'):
        _html += rez['credits']
    return _html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
