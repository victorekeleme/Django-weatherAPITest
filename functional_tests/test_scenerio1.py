from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from functional_tests.test_data import api_display_test_data
from functional_tests import excelUtils
import os
from _datetime import  datetime



class TestScenerio1(StaticLiveServerTestCase):

    #function for setting up the chrome driver
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/driver/chromedriver.exe')

    #function for closing the chrome driver
    def close(self):
        self.browser.close()

    #excel write to file set up
    file = os.path.abspath('functional_tests/result/Results.xlsx')
    sheetNo = 'Sheet1'
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    # test case one
    def test_case1(self):
        try:
            #creating waiting variable
            wait = WebDriverWait(self.browser, 10)
            #open url
            self.browser.get(self.live_server_url)

            #find the city button using XPATH and click on it
            city_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/input[2]')))
            city_btn.click()

            #get the actual city name
            city_name = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1' ))).text.split()[-1]


            #get the expected city name from test data
            test_data = api_display_test_data(city_name)


            #check if expected city name equals actual city name
            if test_data['city_name'] == city_name:
                excelUtils.writeData(self.file, self.sheetNo, 9, 7, test_data['city_name']) #expected result
                excelUtils.writeData(self.file, self.sheetNo, 9, 8, city_name) #actual result
                excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test passed') #status
                excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'Victor Ekeleme\n {self.time}') #comment

                print('pass')

            else:
                excelUtils.writeData(self.file, self.sheetNo, 9, 7, test_data['city_name'])#expected
                excelUtils.writeData(self.file, self.sheetNo, 9, 8, city_name)#actual result
                excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed') #status
                excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'Victor Ekeleme\n {self.time}') #comment

                print('fail')


        except Exception as e:
            #if any error print for debuging purposes
            excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'{e}')  # comment
            excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed')  # status

            print(e)

        finally:
            #close chrome driver after execution
            self.close()

    # test case two
    def test_case2(self):
        try:
            #creating waiting variable
            wait = WebDriverWait(self.browser, 10)

            #open url
            self.browser.get(self.live_server_url)

            #find the city button using XPATH and click on it
            city_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/input[2]')))
            city_btn.click()

            #get the actual city name
            city_name = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1' ))).text.split()[-1]

            #get the expected city name from test data
            test_data = api_display_test_data(city_name)

            #check if expected city name equals actual city name
            self.assertEquals(test_data['city_name'], city_name)

            #get the actual temperature
            temp = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'temp'))).text.split()[-1]

            #check if expected temperature equals actual temperature in degree celcius(°C)
            if test_data['temp'] == temp:
                excelUtils.writeData(self.file, self.sheetNo, 10, 7, test_data['temp'])#expected result
                excelUtils.writeData(self.file, self.sheetNo, 10, 8, temp) #actual result
                excelUtils.writeData(self.file, self.sheetNo, 10, 9, 'test passed') #status
                excelUtils.writeData(self.file, self.sheetNo, 10, 10, f'Victor Ekeleme\n {self.time}') #comment

                print('pass')
            else:
                excelUtils.writeData(self.file, self.sheetNo, 10, 7, test_data['temp']) #expected result
                excelUtils.writeData(self.file, self.sheetNo, 10, 8, temp) #actual result
                excelUtils.writeData(self.file, self.sheetNo, 10, 9, 'test passed') #status
                excelUtils.writeData(self.file, self.sheetNo, 10, 10, f'Victor Ekeleme\n {self.time}') #comment

                print('fail')

        except Exception as e:
            #if any error print for debuging purposes
            excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'{e}')  # comment
            excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed')  # status

            print(e)

        finally:
            #close chrome driver after execution
            self.close()

    #test case three
    def test_case3(self):
        try:
            #creating waiting variable
            wait = WebDriverWait(self.browser, 10)

            #open url
            self.browser.get(self.live_server_url)

            #find the city button using XPATH and click on it
            city_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/input[2]')))
            city_btn.click()

            #get the actual city name
            city_name = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1' ))).text.split()[-1]

            #get the expected city name from test data
            test_data = api_display_test_data(city_name)

            #check if expected city name equals actual city name
            self.assertEquals(test_data['city_name'], city_name)

            #get the actual humidity
            humidity = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'humidity'))).text.split()[-1]

            #check if expected humidity equals actual humidity
            if test_data['humidity'] == humidity:
                excelUtils.writeData(self.file, self.sheetNo, 11, 7, test_data['humidity'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 11, 8, humidity)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 11, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 11, 10, f'Victor Ekeleme\n {self.time}')  # comment

                print('pass')
            else:
                excelUtils.writeData(self.file, self.sheetNo, 11, 7, test_data['humidity'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 11, 8, humidity)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 11, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 11, 10, f'Victor Ekeleme\n {self.time}')  # comment

        except Exception as e:
            #if any error print for debuging purposes
            excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'{e}')  # comment
            excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed')  # status

            print(e)

        finally:
            #close chrome driver after execution
            self.close()

    #test case four
    def test_case4(self):
        try:
            #creating waiting variable
            wait = WebDriverWait(self.browser, 10)

            #open url
            self.browser.get(self.live_server_url)
            #find the city button using XPATH and click on it

            city_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/input[2]')))
            city_btn.click()
            #get the actual city name

            city_name = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1' ))).text.split()[-1]
            #get the expected city name from test data

            test_data = api_display_test_data(city_name)
            #check if expected city name equals actual city name

            self.assertEquals(test_data['city_name'], city_name)

            #get the actual description
            desc = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'description'))).text.split()[-2:]
            description = ' '.join(desc)

            #check if expected description equals actual description
            if test_data['description'] == description:
                excelUtils.writeData(self.file, self.sheetNo, 12, 7, test_data['description'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 12, 8, description)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 12, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 12, 10, f'Victor Ekeleme\n {self.time}')  # comment

                print('pass')
            else:
                excelUtils.writeData(self.file, self.sheetNo, 12, 7, test_data['description'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 12, 8, description)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 12, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 12, 10, f'Victor Ekeleme\n {self.time}')  # comment
                print('fail')

        except Exception as e:
            #if any error print for debuging purposes
            excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'{e}')  # comment
            excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed')  # status

            print(e)

        finally:
            #close chrome driver after execution
            self.close()

    #test case five
    def test_case5(self):
        try:
            #creating waiting variable
            wait = WebDriverWait(self.browser, 10)

            #open url
            self.browser.get(self.live_server_url)

            #find the city button using XPATH and click on it

            city_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/input[2]')))
            city_btn.click()

            #get the actual city name
            city_name = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1' ))).text.split()[-1]

            #get the expected city name from test data
            test_data = api_display_test_data(city_name)

            #check if expected city name equals actual city name
            self.assertEquals(test_data['city_name'], city_name)

            #get the actual minimum temperature
            temp_min = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'temp_min'))).text.split()[-1]

            #check if expected minimum temperature equals actual minimum temperature
            if test_data['temp_min'] == temp_min:
                excelUtils.writeData(self.file, self.sheetNo, 13, 7, test_data['temp_min'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 13, 8, temp_min)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 13, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 13, 10, f'Victor Ekeleme\n {self.time}')  # comment

                print('pass')
            else:
                excelUtils.writeData(self.file, self.sheetNo, 13, 7, test_data['temp_min'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 13, 8, temp_min)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 13, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 13, 10, f'Victor Ekeleme\n {self.time}')  # comment

                print('fail')


        except Exception as e:
            #if any error print for debuging purposes
            excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'{e}')  # comment
            excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed')  # status

            print(e)

        finally:
            #close chrome driver after execution
            self.close()

    #test case six
    def test_case6(self):
        try:
            #creating waiting variable
            wait = WebDriverWait(self.browser, 10)

            #open url
            self.browser.get(self.live_server_url)

            #find the city button using XPATH and click on it
            city_btn = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/input[2]')))
            city_btn.click()

            #get the actual city name
            city_name = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1' ))).text.split()[-1]

            #get the expected city name from test data
            test_data = api_display_test_data(city_name)

            #check if expected city name equals actual city name
            self.assertEquals(test_data['city_name'], city_name)

            #get the actual maximum temperature
            temp_max = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'temp_max'))).text.split()[-1]

            #check if expected maximum temperature equals actual maximum temperature
            if test_data['temp_max'] == temp_max:
                excelUtils.writeData(self.file, self.sheetNo, 14, 7, test_data['temp_max'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 14, 8, temp_max)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 14, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 14, 10, f'Victor Ekeleme\n {self.time}')  # comment

                print('pass')
            else:
                excelUtils.writeData(self.file, self.sheetNo, 14, 7, test_data['temp_max'])  # expected result
                excelUtils.writeData(self.file, self.sheetNo, 14, 8, temp_max)  # actual result
                excelUtils.writeData(self.file, self.sheetNo, 14, 9, 'test passed')  # status
                excelUtils.writeData(self.file, self.sheetNo, 14, 10, f'Victor Ekeleme\n {self.time}')  # comment

                print('fail')

        except Exception as e:
            #if any error print for debuging purposes
            excelUtils.writeData(self.file, self.sheetNo, 9, 10, f'{e}')  # comment
            excelUtils.writeData(self.file, self.sheetNo, 9, 9, 'test failed')  # status

            print(e)

        finally:
            #close chrome driver after execution
            self.close()




