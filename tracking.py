import requests
from bs4 import BeautifulSoup
from translate import Translator
from dotenv import load_dotenv
import os

load_dotenv()

TRACK_NUMBER_ZD = os.getenv('TRACK_NUMBER_ZD')

def get_status():
    data = {'documentCode': TRACK_NUMBER_ZD}
    url = 'http://118.24.145.30:8082/trackIndex.htm'
    response = requests.post(url, data=data)

    soup = BeautifulSoup(response.text, 'lxml')

    local_date, local_time = soup.select('ul.clearfix li.div_li2')[1].text[:-1].split()
    last_status = soup.select('ul.clearfix li.div_li4')[1].text.replace(' ', '')[:-3]

    translator = Translator(from_lang='zh', to_lang='ru')
    last_status = translator.translate(str(last_status))
    return f'**{local_time}**\n{local_date}\n"{last_status}"'

