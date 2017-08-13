import win32con
import win32clipboard
import win32api
import time

StartWait = 10
StartNum = 1272
Inteval = 4

def setText(aString):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    win32clipboard.CloseClipboard()

def sendText():
	win32api.keybd_event(17,0,0,0) # ctrl
	win32api.keybd_event(86,0,0,0) # v
	win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
	time.sleep(0.1)
	win32api.keybd_event(13,0,0,0) # enter
	win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)


time.sleep(StartWait)
while True:
	StrText = str(StartNum) + '只羊，咩咩叫'
	setText(StrText)
	sendText()
	time.sleep(Inteval)
	StartNum += 2