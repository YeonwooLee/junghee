import pyautogui

class noErrorException(Exception):
    def __init__(self):
        self.msg = '그냥 진행시키는 예외'
    def __str__(self) -> str:
        exception_msg = "Message: %s\n" % self.msg
        return exception_msg
class NonePositionException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self) -> str:
        exception_msg = "Message: %s\n" % self.msg
        return exception_msg


#file_img를 talkroom_img로 durationTime에 걸쳐서 드래그앤 드롭
def fileDrag(file_img,talkroom_img,durationTime):
    start_position = pyautogui.locateOnScreen(file_img, confidence=0.95)
    end_position = pyautogui.locateOnScreen(talkroom_img)
    print("start_position=",start_position)
    print("end_position=", end_position)
    if start_position==None:
        raise NonePositionException("화면에 파일 위치가 보이지 않음")
    if end_position==None:
        raise NonePositionException("화면에 카톡방 위치가 보이지 않음")

    pyautogui.moveTo(start_position)
    pyautogui.dragTo(end_position, duration=durationTime)

def temp_ticket():
    pyautogui.click

def main():

    fileDrag('img_KpBid.png','jhin.png',2)

if __name__ == "__main__":
    main()
