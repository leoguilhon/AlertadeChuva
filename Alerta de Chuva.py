import pyautogui as pat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Alerta de Chuva

navegador = webdriver.Chrome()

navegador.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/321/riodejaneiro-rj")
chuva = navegador.find_element("xpath",'//*[@id="mainContent"]/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div/span').get_attribute("data-value")
print(chuva)