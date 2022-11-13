import keyListener
import pyautogui
import time
import mouse
import datetime
import gui_tool
import requests
import selenium.common.exceptions
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import kakao_sender
import my_util


# python -m pip install --upgrade pip
# pip install pyautogui
# pip install pip install pypiwin32
# pip install bs4
# pip install pynput
# pip install mouse
# pip install webdriver_manager
# pip install opencv-python
def driver_quit(driver):
    driver.close()
    driver.quit()
    print("driver_quit SUCCESS!")


def page_parse(page, index):
    print(datetime.datetime.now())
    # url = page['url'].format(page['start_index'])
    url = page["url_complete"]
    # print(url)

    # 드라이버 구성
    option = webdriver.ChromeOptions()

    option.headless = False

    option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/94.0.4606.61 Safari/537.36')

    go_more_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div/div[4]/div[2]/div[2]/div/div[1]/a')))

    go_more_button.click()

    pop_second = driver.find_element(by=By.XPATH, value='// *[ @ id = "sc-button-6"]')  # 2번팝업
    pop_second.click()

    driver.switch_to.frame(driver.find_element(by=By.XPATH, value='//*[@id="openFrame"]'))


def configDriver(show):
    ### 필수 코어 ###
    # 드라이버 구성
    option = webdriver.ChromeOptions()

    # 화면 볼게요
    if show==1:
        option.headless = False
    elif show==0:
        option.headless = True

    option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/94.0.4606.61 Safari/537.36')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    # #driver.fullscreen_window()
    # driver.set_window_position(0, 0)
    # driver.set_window_size(1800, 900)

    # driver.implicitly_wait(120)

    return driver
    ### 필수 코어 ###


def findElementXpath(driver,time,xpath):
    #global driver
    element = WebDriverWait(driver, time).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath)))
    return element

# 30초까지 기다리는 로직을 포함한 element 클릭하는 함수
# xpath = xpath
def clickElement(driver,xpath):
    #global driver
    go_more_button = findElementXpath(driver,90,xpath)

    go_more_button.click()


# 30초까지 기다리는 로직 없이 element 클릭하는 함수
# xpath = xpath
def clickElement2(driver,xpath):
    #global driver
    go_bid_button = driver.find_element(by=By.XPATH, value=xpath)  # 2번팝업
    go_bid_button.click()

# 30초까지 기다리는 로직 없이 element 클릭하는 함수
# xpath = xpath
def clickElement3(driver,xpath):
    #global driver
    go_bid_button = driver.find_element(by=By.XPATH, value=xpath)  # 2번팝업
    go_bid_button.execute_script("arguments[0].click();", go_bid_button)



#화면에 img가 보이면 {true,imageposition}  리턴
def imgExist(img):
    result = {'exist': False}
    imgPosition = pyautogui.locateOnScreen(img, confidence=0.95)
    if imgPosition != None:
        result['exist'] = True
        result['imgPosition'] = imgPosition
    return result

#화면에 img가 보이면 {true,imageposition}  리턴
def imgExistWithConfidence(img,confidenceRate):
    result = {'exist': False}
    imgPosition = pyautogui.locateOnScreen(img, confidence=confidenceRate)
    if imgPosition != None:
        result['exist'] = True
        result['imgPosition'] = imgPosition
    return result

def mouseToImgAndClick(img):
    while True:
        imgPosition = pyautogui.locateOnScreen(img, confidence=0.95)
        if imgPosition != None:
            break
        else:
            print("searching")
    print("imgPosition is = ", imgPosition)
    pyautogui.moveTo(imgPosition)
    pyautogui.click()


def mouseToImgAndClick2(img):
    while True:
        imgExistRst = imgExist(img)
        if imgExistRst['exist']:
            print("imgPosition is = ", imgExistRst['imgPosition'])
            pyautogui.moveTo(imgExistRst['imgPosition'])
            pyautogui.click()
            break
        print('searching')
    # time.sleep(2)

def selectorClick():
    fullXpath = '/html/body/div/map/map/area[6]'


def keyboardTrap():
    print("keyboard Wait")
    ctrlBroker = keyListener.KeyListener()  # ctrl 연속 2번 눌려야 탈출
    ctrlBroker.doubleCtrlTrap()


def keyboardTrap2():
    ctrlBroker = keyListener.KeyListener()  # ctrl 연속 1번 눌려야 탈출
    ctrlBroker.oneCtrlTrap()
    # ctrlBroker = None
def serverTimeTrap(driver,h,m,s):

    while True:
        get_time = findElementXpath(driver,30,'//*[@id="time_area"]').text.split(' ')
        hour=get_time[3][:-1]
        min=get_time[4][:-1]
        sec = get_time[5][:-1]
        print(hour,min,sec)
        if h==hour and m==min and s==sec:
            print('The Time!')
            break
    return
def checkFirstIntance(*args):
    f=open('sign.txt','r')
    t=f.readline()
    print('t is',t)
    f.close()
    if '0'in t:
        f = open('sign.txt', 'w')
        f.write('1')
        f.close()
    else:
        for d in args:
            driver_quit(d)
        exit()
if __name__ == "__main__":

	temp = {
	'stopSellingBtn': 'stopSellingBtn.png', # 판매중지 태그 
	'firstChkBox':'firstChkBox.png', # 첫번째 체크박스
	'delProductBtn':'delProductBtn.png',
	'msgBoxDelWarn':'msgBoxDelWarn.png',
	'okayBtn':'msgBoxDelWarnOkay.png',
	'onLoading':'onLoading.png',
	'loading':'loading.png',
	'moreProduct':'moreProduct.png',
	'delErrorMsg':'delErrorMsg.png',
	'delErrorMsg2':'delErrorMsg2.png',
	'dropdown30':'dropdown30.png',
	'select500':'select500.png'
	}

	# while True: #이건 이미지 정확도 체크용코드
	# 	print(imgExistWithConfidence(temp['delErrorMsg'],0.95)['exist'])

	while imgExistWithConfidence(temp['moreProduct'],0.95)['exist']:
		print("\n\n삭제할 상품 존재")

		# 판매중지 태그 클릭
		# keyboardTrap()
		mouseToImgAndClick2(temp['stopSellingBtn'])

		#로딩
		while not imgExistWithConfidence(temp['loading'],0.5)['exist']:
			print(imgExistWithConfidence(temp['loading'],0.5)['exist'])
		print("존재확인1")
		while imgExistWithConfidence(temp['loading'],0.5)['exist']:
			pass
		
		#드롭다운선택
		mouseToImgAndClick2(temp['dropdown30'])
		#500선택
		mouseToImgAndClick2(temp['select500'])
			
		#로딩
		while not imgExistWithConfidence(temp['loading'],0.5)['exist']:
			print(imgExistWithConfidence(temp['loading'],0.5)['exist'])
		print("존재확인1")
		while imgExistWithConfidence(temp['loading'],0.5)['exist']:
			pass

		#전체선택 체크박스 선택
		# keyboardTrap()
		mouseToImgAndClick2(temp['firstChkBox'])
		time.sleep(2) #예의슬립


		# 상품삭제 버튼 클릭
		# keyboardTrap()
		mouseToImgAndClick2(temp['delProductBtn'])
		time.sleep(2) #예의슬립


		#확인버튼 뜰때까지 대기
		while not imgExist(temp['okayBtn'])['exist']:
			pass

		#확인버튼이 삭제불가 메시지와 함께 뜬경우 
		if(imgExist(temp['delErrorMsg'])['exist'] or imgExist(temp['delErrorMsg2'])['exist']):
			mouseToImgAndClick2(temp['okayBtn'])
			print('확인버튼이 삭제불가 메시지와 함께 뜬경우')
			continue

		#삭제경고
		mouseToImgAndClick2(temp['okayBtn'])	


		#처리완료메세지박스
		while not imgExist(temp['okayBtn'])['exist']:
			print("완료메세지")
		#확인버튼이 삭제불가 메시지와 함께 뜬경우 
		if(imgExist(temp['delErrorMsg'])['exist'] or imgExist(temp['delErrorMsg2'])['exist']):
			mouseToImgAndClick2(temp['okayBtn'])
			print('확인버튼이 삭제불가 메시지와 함께 뜬경우')
			continue
		mouseToImgAndClick2(temp['okayBtn'])	

		#로딩
		while not imgExistWithConfidence(temp['loading'],0.5)['exist']:
			print(imgExistWithConfidence(temp['loading'],0.5)['exist'])
		print("존재확인2")
		while imgExistWithConfidence(temp['loading'],0.5)['exist']:
			pass
			