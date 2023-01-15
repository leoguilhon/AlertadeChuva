# Alerta de Chuva

import time

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

contato = 'importante'  # Nome do contato para o qual será enviado o aviso via Whatsapp
# Horário no qual o código será executado e a mensagem será enviada.
hora = '09:00'
# Path das configurações do Chrome
CHROME_DATA_PATH = "user-data-dir=C:\\Users\\Administrador\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

# Definir as configurações do webdriver para o navegador pessoal

options = webdriver.ChromeOptions()
options.add_argument(CHROME_DATA_PATH)

# Coletar a informação


def AlertadeChuva():
    navegador = webdriver.Chrome(
        executable_path='chromedriver.exe', options=options)

    navegador.get(
        "https://www.climatempo.com.br/previsao-do-tempo/cidade/321/riodejaneiro-rj")
    chuva = navegador.find_element(
        "xpath", '//*[@id="mainContent"]/div[4]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div/span').get_attribute("innerText")
    print(chuva)


# Tratar o dado

    chuvaflt = float(chuva.split("mm")[0])
    print(chuvaflt)

# Definir a intensidade da chuva

    tipodechuva = str
    if (chuvaflt == 0):
        tipodechuva = "Não há chuva"
    if (chuvaflt < 5):
        tipodechuva = "Chuva fraca"
    if (chuvaflt >= 5 and chuvaflt <= 25):
        tipodechuva = "Chuva moderada"
    if (chuvaflt > 25 and chuvaflt <= 50):
        tipodechuva = "Chuva forte"
    if (chuvaflt > 50):
        tipodechuva = "Chuva muito forte"
    print(tipodechuva)

# Enviar alerta de chuva
    if (tipodechuva != "Não há chuva"):
        navegador.get("https://web.whatsapp.com/")
        time.sleep(10)
        # Esperar o whatsapp conectar com o QRCode
        while len(navegador.find_elements(By.ID, 'side')) < 1:
            time.sleep(1)
        navegador.find_element(
            "xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(contato)
        navegador.find_element(
            "xpath", '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(Keys.ENTER)
        navegador.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(
            f"Alerta de Chuva! Olá, {contato}! Já pode tirar o seu guarda-chuva do armário, hoje irá chover com uma precipitação de {chuvaflt:.0f}mm na cidade do Rio de Janeiro. Status da chuva: {tipodechuva}.")
        navegador.find_element(
            "xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(5)


schedule.every(1).days.at(hora).do(AlertadeChuva)
while 1:
    schedule.run_pending()
    time.sleep(1)
