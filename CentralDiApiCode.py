from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time


class Centdi:
    def __init__(self, Url,username,password):
       self.username = username
       self.password = password
       self.Url = Url
       
       
    def create_driver_session(session_id, executor_url):
        from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

        # Save the original function, so we can revert our patch
        org_command_execute = RemoteWebDriver.execute

        def new_command_execute(self, command, params=None):
            if command == "newSession":
                # Mock the response
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return org_command_execute(self, command, params)

        # Patch the function before creating the driver object
        RemoteWebDriver.execute = new_command_execute

        new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        new_driver.session_id = session_id

        # Replace the patched function with original function
        RemoteWebDriver.execute = org_command_execute

        return new_driver

    def login(self):
        ozip = "77449"
        dzip = "11386"
        self.webBrowser = webdriver.Chrome('Input/Driver/chromedriver.exe')
        global executor_url
        executor_url = self.webBrowser.command_executor._url
        global session_id 
        session_id = self.webBrowser.session_id
        
        self.webBrowser.get(self.Url)
        #time.sleep(5)
        #user_name_elem = self.webBrowser.find_element_by_xpath("//*[@id='Username']")
        #user_name_elem.clear()
        #user_name_elem.send_keys(self.username)
        #passworword_elem = self.webBrowser.find_element_by_xpath("//*[@id='password']")
        #passworword_elem.clear()
        #passworword_elem.send_keys(self.password)
        #passworword_elem.send_keys(Keys.RETURN)
        #time.sleep(10)
        
        self.webBrowser.get(self.Url)
        #ozip
        #user_name_elem = self.webBrowser.find_element_by_xpath("//*[@id='originZip']")
        #user_name_elem.clear()
        #user_name_elem.send_keys(ozip)
        #dzip
        #user_name_elem =self.webBrowser.find_element_by_xpath("//*[@id='destinationZip']")
        #user_name_elem.clear()
        #user_name_elem.send_keys(dzip)


        #drop = Select(self.webBrowser.find_element_by_xpath("//*[@id='ymmVehicleType0']"))
        #drop.select_by_visible_text('Car')

        #ActionChains(self.webBrowser).send_keys(Keys.F12).perform()

        #self.webBrowser.find_element_by_xpath('//*[@id="postload_form"]/div[8]/div[2]/div[1]/span[1]').click()
       
        print (session_id )
        print (executor_url)
       
        driver2 = Centdi.create_driver_session(session_id, executor_url)
        #print( "Done login" )
        return driver2

           
    def getdata(self,ozip,dzip,types,Key, webBrowser):
        from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
        webBrowser.execute_script("window.open('','secondtab');")
        webBrowser.switch_to.window("secondtab")
        
        Url1 = "https://www.centraldispatch.com/protected/cargo/sample-prices-lightbox?num_vehicles=1&ozip="
        Url2 ="&dzip="    
        Url3 = "&enclosed=0&inop=0&vehicle_types="
        Url4 = "&miles="
        Url5 = Key

        #Url = Url1+ str(ozip) +Url2+ str(dzip) +Url3+ types + Url4 + str(Url5)
        webBrowser.get("https://www.google.com/search?q=gmail&rlz=1C1JJTC_enUS959US960&oq=gmail&aqs=chrome..69i57j0i131i433i512j0i433i512l2j0i131i433i512l2j0i433i512j69i61.884j0j4&sourceid=chrome&ie=UTF-8")
        
        





    


