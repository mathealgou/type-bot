from PIL import ImageGrab
import pytesseract
import pyautogui
import time

def main():
    pyautogui.getWindowsWithTitle('Google Chrome')[0].activate()
    
    time.sleep(1)
    
    bounding_box = (190, 400, 1155, 515)
    image = ImageGrab.grab(bbox=bounding_box)
    
    text = pytesseract.image_to_string(image)
    text = text.replace('\n', ' ')
    
    pyautogui.click(500, 500)
    pyautogui.typewrite(text)
    
if __name__ == '__main__':
	main()