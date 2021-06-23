import requests
import json
from datetime import date

accuweatherAPIKey= 'uyjvS48MxQMIsZAYVxTTiiJ3Zhqw5rDf'

LocationAPIURL =  "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"\
                 +"127164?apikey="+accuweatherAPIKey+"&language=pt-br"

r = requests.get(LocationAPIURL)

if (r.status_code != 200):
    print('Não foi possivel obter codigo!')
else:
    print(json.loads(r.text))


    
