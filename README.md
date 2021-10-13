# IGBOT v2.0
This bot scrapes the web. It requires your Instagram credentials and logs into your account and looks for information on a specified IG profile. Then, it copies links, dumps them into a .txt file and sends an email. 

----------------------------DISCLAIMER------------------------------
All actions are visible on screen on start.
All actions performed by this program are under your responsability.  
----------------------------DISCLAIMER------------------------------


____Procedure to run the program____

1- Have at least version 3.9.1 of python installed

2- Install the corresponding libraries using pip

--- pip install pynput
--- pip install selenium
--- pip install pyperclip
--- pip install time

3- Check the version of your browser (Chrome, Firefox, Internet Explorer, Opera, Safari)

4- Download the corresponding webdriver and place it on the main disk
   (you need to change the file location and webdriver in the program)
   driver = webdriver.PlaceYourBrowserHere (
        executable_path = C:\chromedriver_win32\chromedriver.exe)
   It should be in an accessible folder
   
5- Enjoy!
