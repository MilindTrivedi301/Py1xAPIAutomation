# call the selenium
# use the selenium command

# Selenium Code(Python,Java) -> API HTTP Request -> ChromeDriver / Geckodriver -> chrome/firefox

from selenium import webdriver

# create session
# sen the commands - navigate to a url
#If you are using Selenium <4, We use to set the Driver path
#If you are using the selenium > 4, Driver path is not needed. they will handle automatically
# selenium-4.16.0

browser = webdriver.Chrome()
browser.get("http://app.vwo.com")
