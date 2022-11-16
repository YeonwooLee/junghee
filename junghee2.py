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
# pip install selenium
# pip install packaging


#화면에 img가 보이면 {true,imageposition}  리턴
def imgExistWithConfidence(img,confidenceRate):
    result = {'exist': False}
    imgPosition = pyautogui.locateOnScreen(img, confidence=confidenceRate)
    if imgPosition != None:
        result['exist'] = True
        result['imgPosition'] = imgPosition
    return result

#이미지로 마우스 이동, 클릭
def mouseToImgAndClick2(img):
    while True:
        imgExistRst = imgExist(img)
        if imgExistRst['exist']:
            print("imgPosition is = ", imgExistRst['imgPosition'])
            pyautogui.moveTo(imgExistRst['imgPosition'])
            pyautogui.click()
            break
        print('searching')

#화면에 img가 보이면 {true,imageposition}  리턴
def imgExist(img):
    result = {'exist': False}
    imgPosition = pyautogui.locateOnScreen(img, confidence=0.95)
    if imgPosition != None:
        result['exist'] = True
        result['imgPosition'] = imgPosition
    return result

#나타났다사라짐
def disappear(imgFileName,confidence):
    while not imgExistWithConfidence(imgFileName,confidence)['exist']:
        print(imgFileName+" 의 등장을 기다리는중")
        print(imgExistWithConfidence(imgFileName,confidence)['exist'])
    while imgExistWithConfidence(imgFileName,confidence)['exist']:
        pass

if __name__ == "__main__":
	print("프로그램 시작")

	temp = {
	'stopSellingBtn': 'stopSellingBtn.png', # 판매중지 태그 
	'firstChkBox':'firstChkBox.png', # 첫번째 체크박스(전체선택용)
	'delProductBtn':'delProductBtn.png',# 삭제버튼
	'msgBoxDelWarn':'msgBoxDelWarn.png',# 삭제경고 페이지
	'okayBtn':'msgBoxDelWarnOkay.png',# confirm창 확인버튼
	'onLoading':'onLoading.png',# 로딩중인 그림 -- 사용 x
	'loading':'loading.png', #로딩중인 그림과 로딩중글씨 같이 캡쳐
	'moreProduct':'moreProduct.png',# 수정 밑에 밑줄쳐져있는 수정 글씨 좁게 캡쳐
	'delErrorMsg':'delErrorMsg.png',# 삭제에러 총 두개
	'delErrorMsg2':'delErrorMsg2.png',#삭제 에러 총 두개 --하나로 통일해보기 -- 상품만 가능합니다로
	'dropdown30':'dropdown30.png', #드롭다운 누르기위한 30
	'select500':'select500.png', #설정할 개수
	'nodata':'nodata.png' #다지우면 나오는화면
	}

	# while True: #이건 이미지 정확도 체크용코드
	# 	print(imgExistWithConfidence(temp['delErrorMsg'],0.95)['exist'])

    # 추가상품이 있는 한 계속
	while True:
		# print("\n\n삭제할 상품 존재")

		# 판매중지 태그 클릭
		mouseToImgAndClick2(temp['stopSellingBtn'])
		print("# 판매중지 태그 클릭")

		#로딩창나타났다사라짐
		disappear(temp['loading'],0.5)
		print("#로딩창나타났다사라짐")
		
		#드롭다운선택
		mouseToImgAndClick2(temp['dropdown30'])
		print("#드롭다운선택")
		
		#드롭다운옵션선택
		mouseToImgAndClick2(temp['select500'])
		print("#드롭다운옵션선택")
		
		
		# #로딩
		disappear(temp['loading'],0.5)
		print("#로딩창나타났다사라짐")

		#전체선택 체크박스 선택
		mouseToImgAndClick2(temp['firstChkBox'])
		print("#전체선택 체크박스 선택")
		time.sleep(2) #예의슬립


		# 상품삭제 버튼 클릭
		mouseToImgAndClick2(temp['delProductBtn'])
		print("상품 삭제 버튼 클릭")
		time.sleep(2) #예의슬립


		#확인버튼 뜰때까지 대기
		while not imgExist(temp['okayBtn'])['exist']:
			print("#확인버튼 뜰때까지 대기")
			pass

		#확인버튼이 삭제불가 메시지와 함께 뜬경우 
		if(imgExist(temp['delErrorMsg'])['exist'] or imgExist(temp['delErrorMsg2'])['exist']):
			mouseToImgAndClick2(temp['okayBtn'])
			print('확인버튼이 삭제불가 메시지와 함께 뜬경우')
			continue

		#삭제경고
		mouseToImgAndClick2(temp['okayBtn'])	
		print("#삭제경고어쩌고에 확인 클릭")


		#처리완료메세지박스
		while not imgExist(temp['okayBtn'])['exist']:
			print("완료메세지 뜰때까지 대기중")

		#확인버튼이 삭제불가 메시지와 함께 뜬경우 
		if(imgExist(temp['delErrorMsg'])['exist'] or imgExist(temp['delErrorMsg2'])['exist']):
			mouseToImgAndClick2(temp['okayBtn'])
			print('확인버튼이 삭제불가 메시지와 함께 뜬경우')
			continue

		#삭제되었습니다에 확인 클릭
		mouseToImgAndClick2(temp['okayBtn'])
		print("#삭제되었습니다에 확인 클릭")

		disappear(temp['loading'],0.5)
		print("#로딩창나타났다사라짐")
			
	print("더이상 삭제할 상품이 남아있지 않아 종료합니다")