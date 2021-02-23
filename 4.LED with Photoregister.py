from pyfirmata import Arduino,util
import time

#핀 모드 세팅
board = Arduino('COM8')

analog_input = board.get_pin('a:0:i') # 0번 핀 입력
led = board.get_pin('d:13:o') #13번 핀 출력

it = util.Iterator(board) #회로의 입력상태를 읽어올 변수선언
it.start()

while True:
    analog_value = analog_input.read()
    print(analog_value)
    for i in range(1):
        if analog_value is None:
            time.sleep(3)
            break  
        if analog_value > 0.1:
            led.write(1)
        if analog_value < 0.1:
            led.write(0)
            
