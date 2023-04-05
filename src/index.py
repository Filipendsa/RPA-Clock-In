from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
import datetime


def esta_na_hora(hora, minuto, data_atual):
    if data_atual.hour in hora and data_atual.minute in minuto:
        return True
    return False


def esta_no_dia_da_semana(dias_da_semana, data_atual):
    if data_atual.weekday() in dias_da_semana:
        return True
    return False


dias_da_semana_int = [0, 1, 2, 3, 4]
hora = [12, 13]
hora2 = [7, 17]
minuto = [00]
minuto2 = [30]

browser = webdriver.Chrome()
browser.get("https://www.ahgora.com.br/novabatidaonline/")
list_punches = '["073129"]'
browser.execute_script(
    'localStorage.setItem("@batidaOnline/list_punches","'+list_punches.replace('"', '\\"')+'");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/isSingle","true");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/passwordOnly","false");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/token","0cab6ce4b8908900b6ef7d65bc234161");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/latest_punch_day","2023-04-05");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/defaultDeviceActive","false");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/permitido_timesheet","0");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/breakDevice","false");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/employeeName","Filipe Nogueira da Silva");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/companyCode","641887decdea212d992e6d63");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/ssoOnly","false");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/employeeEnrollment","341");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/companyName","INSTITUTO ADVENTISTA DE ENSINO");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/identity","ecc45bf588cb751128079f44f8de4efb");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/image_base64","");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/employeePassword","76176FN123");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/firstPunch","false");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/permitido_batida_mobile","0");')
browser.execute_script(
    'localStorage.setItem("@batidaOnline/i18nextLng","pt-PT");')
time.sleep(1)
browser.refresh()
time.sleep(1)
while True:
    agora = datetime.datetime.now()
    print(agora)
    if not (esta_no_dia_da_semana(dias_da_semana_int, agora)) or agora.hour > 17 or (agora.weekday() == 4 and agora.hour > 12):
        print('saindo...')
        break

    if agora.minute == 30 or agora.minute == 00:
        if (esta_na_hora(hora, minuto, agora) or esta_na_hora(hora2, minuto2, agora)):
            browser.find_element(
                By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/button').click()
            print('esperando...')
            time.sleep(1800)
    else:
        print('sincronizando...')
        time.sleep(60 - agora.second)
