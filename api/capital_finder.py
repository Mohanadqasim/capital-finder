from urllib import parse
import requests
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_componant = parse.urlsplit(s) # split the url
        qsl = parse.parse_qsl(url_componant.query)
        dic = dict(qsl) # {key:value}
        country = dic.get('country')
        capital = dic.get('capital')
        if country:

            path = f'https://restcountries.com/v3.1/name/{country}'
            r = requests.get(path)
            data = r.json() 
            capital = data[0]['capital'][0]              
            msg = f'The capital of {country} is {capital}'
        
        elif capital:

            path = f'https://restcountries.com/v3.1/capital/{capital}'
            r = requests.get(path)
            data = r.json()
            country = data[0]['name']['common']
            msg = f'The country of {capital} is {country}'
   

        else:
            msg = 'hello from the other side stranger'
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(msg.encode('utf-8'))
        return