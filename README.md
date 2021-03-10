# Arduino example 4
Tutorial 4. LED with Photoresistor \
Photoresistor(Ambient Light Sensor 이용)의 입력 값에 따라 LED가 on/off 되도록 제작

## circuit
LED : digital 13pin \
Photoresistor : analog 0pin\
![image](https://user-images.githubusercontent.com/79436159/108827131-906fe400-7608-11eb-8f8c-900b45b5d1dd.png)

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` import time ```\
프로그램을 일정시간동안 지연시키기위해 time 모듈을 import함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` analog_input = board.get_pin('a:0:i')``` \
  -> 0번핀을 analog신호 입력핀으로 설정\
  ```led = board.get_pin('d:13:o') ```\
  -> 13번 핀을 digital신호 출력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin 
 
 ``` it = util.Iterator(board) ```\
보드의 입력값을 지속적으로 업데이트해주는 iterator 변수 선언

 ``` it.start()``` \
iterator 시작

``` analog_value = analog_input.read() ```\
Photoresistor 연결된 0번핀의 입력을 읽어와서 변수 analog_value에 저장

```\
for i in range(1):
  if analog_value is None: 
    time.sleep(3)
    break  
``` 
입력으로 들어온 analog_value값이 None이면 지연시키고 for문에서 빠져나옴

```
if analog_value > 0.1:
  led.write(1)
if analog_value < 0.1:
  led.write(0) 
```
analog_value값이 0.1보다 크면 led가 켜지도록 1을 입력으로 줌\
analog_value값이 0.1보다 작으면 led가 꺼지도록 0을 입력으로 줌

