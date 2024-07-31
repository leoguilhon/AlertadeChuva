from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import schedule

contato = ['Importante']
hora = '22:19'
CHROME_DATA_PATH = "user-data-dir=C:\\Users\\Administrador\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

options = Options()
options.add_argument(CHROME_DATA_PATH)

def AlertadeChuva():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)

    navegador.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/321/riodejaneiro-rj")
    chuva = navegador.find_element(By.XPATH, '//*[@id="mainContent"]/div[7]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div/span').get_attribute("innerText")
    print(chuva)

    chuvaflt = float(chuva.split("mm")[0])
    print(chuvaflt)

    if chuvaflt == 0:
        tipodechuva = "Não há chuva"
    elif 0 < chuvaflt < 5:
        tipodechuva = "Chuva fraca"
    elif 5 <= chuvaflt <= 25:
        tipodechuva = "Chuva moderada"
    elif 25 < chuvaflt <= 50:
        tipodechuva = "Chuva forte"
    else:
        tipodechuva = "Chuva muito forte"
    print(f"Tipo de chuva: {tipodechuva}")

    if chuvaflt > 0:
        navegador.get("https://web.whatsapp.com/")
        time.sleep(12)
        while len(navegador.find_elements(By.ID, 'side')) < 1:
            time.sleep(1)
        for x in contato:
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').clear()
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(x)
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(f"Alerta Diário de Chuva! Olá, {x}! De acordo com o ClimaTempo, hoje poderá ocorrer {tipodechuva}, com precipitação média de {chuvaflt:.0f}mm na cidade do Rio de Janeiro.")
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
            print(f"Mensagem enviada para {x}!")
            time.sleep(5)
    else:
        print("Hoje não chove.")
        navegador.get("https://web.whatsapp.com/")
        time.sleep(12)
        while len(navegador.find_elements(By.ID, 'side')) < 1:
            time.sleep(1)
        for x in contato:
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').clear()
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(x)
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys("Alerta Diário de Chuva! De acordo com o ClimaTempo, hoje não irá chover na cidade do Rio de Janeiro.")
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
            print(f"Mensagem enviada para {x}!")
            time.sleep(5)
    print("Aguardando o próximo horário de envio.")

schedule.every(1).days.at(hora).do(AlertadeChuva)
while 1:
    schedule.run_pending()
    time.sleep(1)
