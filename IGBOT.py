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
    print("Please disable two factor auth (function not supported)")
    print("  ")
    username = input(
        str("Enter your username: "))
    pw = getpass_ak.getpass("Enter your password: ")
    mail = input(
        str("Enter an email to send recovered links: "))
    user = input(str("Enter IG user to retrieve posts: "))
    ctd = int(input("Enter the number of posts you want: "))

    links.append("Page: " + user)
    links.append(" ")


def login(username, pw):
    global driver
    driver = webdriver.Chrome(
        executable_path="C:\chromedriver_win32\chromedriver.exe")
    driver.get(web)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.find_element_by_name("username").send_keys(username)  # User
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(pw)  # Password
    time.sleep(2)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()  # Login button
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()    # Jump pop ups
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()    # Jump pop ups


def scrape():
    driver.get(web + user)
    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div')\
        .click()  # Get last post

    for i in range(0, ctd):
        x = driver.current_url
        time.sleep(1)
        links.append(x)
        time.sleep(1)
        keyboard.tap(Key.space)
        time.sleep(1)
        keyboard.tap(Key.right)  # Next post
        time.sleep(1)
    keyboard.tap(Key.esc)


def text():
    with open("info.txt", 'w') as output:
        for row in links:
            output.write(str(row) + '\n')


def logout():

    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')\
        .click()  # Profile
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
