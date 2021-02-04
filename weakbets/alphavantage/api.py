import weakbets.alphavantage.apikey

# main library for API requests
import requests

# JSON for API result parsing
import json

def reload():
    import importlib
    importlib.reload(weakbets.alphavantage.apikey)

#
# API config
#

URL = 'https://alpha-vantage.p.rapidapi.com/query'

HEADERS = {
        'x-rapidapi-key': weakbets.alphavantage.apikey.APIKEY,
        'x-rapidapi-host': 'alpha-vantage.p.rapidapi.com',
        }


#
# Individual API requests
#

def global_quote(symbol):
    q = {'function': 'GLOBAL_QUOTE', 'symbol': symbol}
    response = requests.request('GET', URL, headers=HEADERS, params=q)
    if response.status_code == 200:
        j = json.loads(response.text)
        glob = j['Global Quote']
        symb = glob['01. symbol']
        opn  = glob['02. open']
        high = glob['03. high']
        low  = glob['04. low']
        pric = glob['05. price']
        volu = glob['06. volume']
        #prev = glob['08. previous close']
        chng = glob['09. change']
        chpr = glob['10. change percent']
        return f'{symb}: ${pric} (${low} .. ${high}), open: ${opn}, change: ${chng} ({chpr}), volume: {volu}'
    else:
        print(response.status_code, response.text)
        return 'Something went wrong.'
