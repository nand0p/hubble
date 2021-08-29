from flask import Flask, request
import requests
import random


image_count = 4670
image_show = 5
#api_endpoint = 'https://hubblesite.org/api/v3/image/'
api_endpoint = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count='  + str(image_show)

app = Flask(__name__)


@app.route('/')
def home():
    html = get_header()

    try:
      rez = requests.get(api_endpoint)
      for count in range(1, image_show):
        html += get_image(rez[count])
      html += get_footer()
      return html

    except:
      html += 'service not available'
      return html



def get_footer():
    return '<p>This site refreshes every 20 seconds with new images from the NASA Hubble Telescope archives' + \
           '<p>Source Code: <a href=https://github.com/nand0p/hubble>https://github.com/nand0p/hubble</a>' + \
           '<p>If you find this useful, please contribute:<br><b>' + \
           'BTC: 112JJvxsvRYn4QtpWJqZmLsTbPEG7aPsdB<br>' + \
           'ETH: 0x5b857cc1103c82384457BACdcd6E2a9FCD0b7e2A</b>' + \
           '<p>SEDME -- Hex7 Internet Solutions<p><b>&copy;2020 </b>' + \
           '<a target=_blank href=http://hex7.com><b>Hex 7 Internet Solutions</b></a><br>' + \
           request.headers.get('User-Agent') + ' -- ' + get_ip() + '</font></body></html>'

def get_header():
    return '<html><head><title>NASA Image SlideShow</title><meta http-equiv=refresh content=20>' + \
           '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-32710227-3"></script>' + \
           '<script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} ' + \
           'gtag("js", new Date()); gtag("config", "UA-32710227-3"); </script>' + \
           '<script data-ad-client="ca-pub-9811914588681081" async ' + \
           'src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>' + \
           '</head><body bgcolor="black"><font color="white">'

def get_ip():
    if request.headers.get("X-Forwarded-For"):
        return request.headers.get("X-Forwarded-For").split(,)[0]
    else:
        return request.remote_addr

def get_image(rez):
    _html = '<b>' + rez.get('title') + '</b> ' + '<br>'
    _html += '<img src=' + rez.get('url') + ' height=95%><br>' + rez.get('url') + '<p>'
    if rez.get('explanation'):
        _html += '<p>' + rez.get('explanation')
    if rez.get('copyright'):
        _html += '<p>Credits: ' + rez.get('copyright')
    _html += '<p><br><p><hr><hr><p><br>'
    return _html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
