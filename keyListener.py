import pyautogui
from pynput import keyboard

class KeyListener:
    def __init__(self):
        self.ctrlLInterrupted = 0
    #키보드내려감
    def on_press(self,key):
        try:
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
        except AttributeError:
            print('special key pressed: {0}'.format(
                key))
    #키보드 올라감
    def on_release(self,key):
        print('Key released: {0}'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    #키보드내려간 입력 연속 두번 ctrl.l이면 종료
    def doubleCtrl(self,key):
        try:
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
            self.ctrlLInterrupted=0
        except AttributeError:
            print('special key pressed: {0}'.format(
                key))

            if key==keyboard.Key.ctrl_l:
                self.ctrlLInterrupted+=1
                print("ctrlLInterrupted",self.ctrlLInterrupted)
                if self.ctrlLInterrupted==2:
                    print('double Ctrl!')
                    return False
            else:
                self.ctrlLInterrupted=0
                if key == keyboard.Key.shift:
                    pyautogui.press('enter')

    #ctrl.l이면 종료
    def oneCtrl(self,key):
        try:
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
            self.ctrlLInterrupted=0
        except AttributeError:
            print('special key pressed: {0}'.format(
                key))

            if key==keyboard.Key.ctrl_l:
                self.ctrlLInterrupted+=1
                print("ctrlLInterrupted",self.ctrlLInterrupted)
                if self.ctrlLInterrupted==1:
                    print('one Ctrl!')
                    return False
            else:
                self.ctrlLInterrupted=0
                if key == keyboard.Key.shift:
                    pyautogui.press('enter')

    def doubleCtrlTrap(self):
        # # Collect events until released
        with keyboard.Listener(
                on_press=self.doubleCtrl,
                on_release=self.on_release) as listener:
            listener.join()
    def oneCtrlTrap(self):
        # # Collect events until released
        with keyboard.Listener(
                on_press=self.oneCtrl,
                on_release=self.on_release) as listener:
            listener.join()
