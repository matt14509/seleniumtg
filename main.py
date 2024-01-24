from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service
import json
import requests
import datetime


numberteletest = '6283898514747'
item_idtgtest = '96845541'
# Bearer ваш токен
headers = {
    "accept": "application/json",
    "authorization": "Bearer "
}
datetime.time()
# телеграм
# ДЛЯ АВТОРЕГОВ ПОЛУКАЧЕСТВО ПЕРЕПРОДАЖА: https://api.lzt.market/telegram?password=no&pmin=0&pmax=20&auction=no&sb_by_me=false&nsb_by_me=true&title=%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%B3&order_by=price_to_up
# ДЛЯ ВСЕГО: https://api.lzt.market/telegram?password=no&pmin=0&pmax=15&auction=no&sb_by_me=false&nsb_by_me=true&order_by=price_to_up
# ДЛЯ АВТОРЕГОВ КАЧЕСТВО: https://api.lzt.market/telegram?password=%D1%82%D1%89&origin[]=autoreg&sb_by_me=false&nsb_by_me=true&order_by=price_to_up
url3 = "https://api.lzt.market/telegram?password=%D1%82%D1%89&origin[]=autoreg&sb_by_me=false&nsb_by_me=true&order_by=price_to_up"
response3 = requests.get(url3, headers=headers)
json_data3 = json.loads(response3.text)
item_idtg = json_data3['items'][0]['item_id']
pricetg = json_data3['items'][0]['price']
print("Ид на маркете telegram:", item_idtg)
print("Цена на маркете telegram:", pricetg)
# вк
# ДЛЯ ПЕРЕПРОДАЖИ И БРУТА : https://api.lzt.market/vkontakte?tel=yes&tfa=no&token_auth_only=no&opened_profile=true&pmin=0&pmax=23&origin[]=brute&origin[]=resale&sb_by_me=false&nsb_by_me=true&order_by=price_to_up
# ДЛЯ ВСЕГО : https://api.lzt.market/vkontakte?tel=yes&tfa=no&token_auth_only=no&pmin=0&pmax=13&auction=no&sb_by_me=false&nsb_by_me=true
# ДЛЯ БРУТА: https://api.lzt.market/vkontakte?tel=yes&tfa=no&token_auth_only=no&opened_profile=true&auction=no&origin[]=brute&sb_by_me=false&nsb_by_me=true&order_by=price_to_up

url4 = f"https://api.lzt.market/{item_idtg}/fast-buy?price={pricetg}"
response4 = requests.post(url4, headers=headers)
json_data4 = json.loads(response4.text)
phonetg = json_data4['item']['telegram_phone']
print("Значение phone telegram:", phonetg)
s = Service(executable_path='J:\programming\geckodriver-v0.33.0-win64\geckodriver.exe')
driver = webdriver.Firefox(service=s)
try:

    driver.maximize_window()

    driver.get('https://web.telegram.org/k/')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/button[1]').click()
    driver.implicitly_wait(5)
    telewebnum = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]')
    telewebnum.clear()
    telewebnum.send_keys(phonetg)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[1]/div').click()
    time.sleep(5)
    url5 = f"https://api.lzt.market/{item_idtg}/telegram-login-code"
    response5 = requests.get(url5, headers=headers)
    json_data5 = json.loads(response5.text)
    codes = json_data5['codes']
    sorted_codes = sorted(codes, key=lambda x: x['date'], reverse=True)
    last_code = sorted_codes[0]['code']
    print('Последний по времени code:', last_code)
    codetelegrame = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[4]/div/div[3]/div/input')
    codetelegrame.clear()
    codetelegrame.send_keys(last_code)




except Exception as ex:
    print(ex)
finally:

    cookies = driver.get_cookies()
    print(cookies)
    datetime.time()
    print(f'https://lzt.market/{item_idtg}/')
    print("final")
