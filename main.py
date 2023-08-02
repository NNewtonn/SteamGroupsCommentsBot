from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")
mensaje = "RBEP es un grupo español dedicado a la simulación militar en Arma 3, aspiramos a la diversion ordenada y la competicion.\n\nCon nosotros aprenderas en profundidad, somos instruidos por gente de toda Europa como miembros de los Royal Welsh.\n\nParticipamos en una comunidad pvp internacional donde se jugan partidas de 100 jugadores todos los viernes, si eso suena como diversion para ti, ya sabes\n\nNuestros horarios son los domingos 17:00.\n\nDISCORD: https://discord.gg/HywB6kyKRC (Newton#3868)\n\nVideo por si quereis saber un poco mas de nosotros\n\n(Todo esta grabado en medio de nuestras operaciones)\n\nhttps://youtu.be/PkLzNGlunhwAac"
webs = ["https://steamcommunity.com/groups/arma3_es", "https://steamcommunity.com/groups/spainarma3", "https://steamcommunity.com/groups/arma3argentina"]
user = "New"  # cba | New | Ali
iniciar = 0


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
value = 1
cookies = []
action = ActionChains(driver)


if (iniciar):

    # Guardar datos de inicio de sesion
    print('Iniciando guardar cookies')
    driver.get("https://steamcommunity.com/groups/arma3_es")
    time.sleep(120)
    if (user != "New"):
        pickle.dump(driver.get_cookies(), open("cookies2.pkl", "wb"))
    else:
        pickle.dump(driver.get_cookies(), open("cookies1.pkl", "wb"))
    print('Cookies guardadas')
    

driver.get("https://steamcommunity.com/groups/arma3_es")
if (user != "New"):
    cookies = pickle.load(open("cookies2.pkl", "rb"))
    print("Cargando cookies de Cbanyuls")
else:
    cookies = pickle.load(open("cookies1.pkl", "rb"))
    print("Cargando cookies de newton")
for cookie in cookies:
    driver.add_cookie(cookie)


def postear(web):
        clanid = ["103582791434557802", "103582791434080466", "103582791434083979"]
        time.sleep(2)
        driver.get(web)

        time.sleep(14)
        print('//*[@id="commentthread_Clan_{clanid[1]}_posts"]')
        if (web == webs[0]):
            ultimo_comentario = driver.find_element(
                "xpath", f'//*[@id="commentthread_Clan_{clanid[0]}_posts"]')
            comentarios = driver.find_elements(
                "xpath", f'//*[@id="commentthread_Clan_{clanid[0]}_posts"]')
        elif (web == webs[1]):
            ultimo_comentario = driver.find_element(
                "xpath", f'//*[@id="commentthread_Clan_{clanid[1]}_posts"]')  #//*[@id="commentthread_Clan_103582791434080466_posts"]
            comentarios = driver.find_elements(
                "xpath", f'//*[@id="commentthread_Clan_{clanid[1]}_posts"]')
        else:
            ultimo_comentario = driver.find_element(
                "xpath", f'//*[@id="commentthread_Clan_{clanid[2]}_posts"]')  #//*[@id="commentthread_Clan_103582791434083979_posts"]
            comentarios = driver.find_elements(
                "xpath", f'//*[@id="commentthread_Clan_{clanid[2]}_posts"]')
        print(ultimo_comentario.text[0:3])
        id_ultimo_comentario = ultimo_comentario.text[0:3]
        time.sleep(9)
        if (id_ultimo_comentario != user):
            #Hacer aleatorio los tiempos de respuesta
            print("Tirando loteria de tiempo:")
            if random.randint(0, 100) < 10:
                print("Tirada de 340 segundos.")
                time.sleep(5)
            elif random.randint(0, 100) < 25:
                print("Tirada de 200 segundos.")
                time.sleep(5)
            else:
                print("Tirada de 60 segundos.")
                time.sleep(5)
            if (web == webs[0]):
                para_borrar = driver.find_element(
                    "xpath", '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/div[2]/div/div[2]/div[2]')
                boton = driver.find_element(
                    "xpath", '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/div[2]/div/div[2]/div[2]/div[1]/div/a/img')
            elif (web == webs[1]):
                para_borrar = driver.find_element(
                    "xpath", '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/div[2]/div/div[2]/div[2]')
                boton = driver.find_element(
                    "xpath", '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/div[2]/div/div[2]/div[2]/div[1]/div/a/img')
            else:
                para_borrar = driver.find_element(
                    "xpath", '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/div[2]/div/div[2]')
                boton = driver.find_element(
                    "xpath", '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/div[2]/div/div[2]/div[2]/div[1]/div/a/img')




            ActionChains(driver).move_to_element(para_borrar).perform()
            ActionChains(driver).move_to_element(boton).click().perform()

            time.sleep(9)
            if (web == webs[0]):
                inputElement = driver.find_element(
                    "xpath", f'//*[@id="commentthread_Clan_{clanid[0]}_textarea"]')
            elif (web == webs[1]):
                inputElement = driver.find_element(
                    "xpath", f'//*[@id="commentthread_Clan_{clanid[1]}_textarea"]')
            else:
                inputElement = driver.find_element(
                    "xpath", f'//*[@id="commentthread_Clan_{clanid[2]}_textarea"]')
            time.sleep(2)
            print("Escribiendo mensaje... (Jodete Austinz maricon)")
            inputElement.send_keys(mensaje)
            if (web == webs[0]):
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="commentthread_Clan_{clanid[0]}_submit"]'))).click()
            elif (web == webs[1]):
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="commentthread_Clan_{clanid[1]}_submit"]'))).click()
            else: 
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="commentthread_Clan_{clanid[2]}_submit"]'))).click()
        else:
            #print("El ultimo comentario es mio")
        # value = False
            time.sleep(25)

while (value):
   #postear(webs[2])
   postear(webs[1])
   #postear(webs[0])


driver.quit()
