from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import time
import pyperclip as pc
from pack import getpass_ak
from pack import send_mail

links = []
keyboard = Controller()


def info():
    global username, pw, web, user, ctd, mail
    web = "https://www.instagram.com/"
    print("IGBOT")
    print("Por favor, deshabilite la verificación en dos pasos por el momento.")
    print("  ")
    username = input(
        str("Ingrese su Usuario, telefono o correo electrónico: "))
    pw = getpass_ak.getpass("Ingrese su contraseña: ")
    mail = input(
        str("Ingrese el correo al que quiera enviar los links recopilados: "))
    user = input(str("Ingrese al usuario que quiere buscar: "))
    ctd = int(input("Ingrese el número de posts que quiere guardar: "))

    links.append("Pagina: " + user)
    links.append(" ")


def login(username, pw):
    global driver
    driver = webdriver.Chrome(
        executable_path="C:\chromedriver_win32\chromedriver.exe")
    driver.get(web)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.find_element_by_name("username").send_keys(username)  # Usuario
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(pw)  # Contraseña
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()  # Botón de login
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()    # Saltar popups
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()    # Saltar popups


def scrape():
    driver.get(web + user)
    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div')\
        .click()  # encontrar último post de la página

    for i in range(0, ctd):
        x = driver.current_url
        time.sleep(1)
        links.append(x)
        time.sleep(1)
        keyboard.tap(Key.space)
        time.sleep(1)
        keyboard.tap(Key.right)  # Siguiente post
        time.sleep(1)
    keyboard.tap(Key.esc)


def text():
    with open("info.txt", 'w') as output:
        for row in links:
            output.write(str(row) + '\n')


def logout():

    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')\
        .click()  # Perfil
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div')\
        .click()  # Log out
    time.sleep(1)
    driver.quit()  # close tab


info()
login(username, pw)
scrape()
text()
logout()
send_mail.send(mail)
