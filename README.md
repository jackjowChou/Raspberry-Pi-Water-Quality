# Raspberry-Pi-Water-Quality
使用 樹莓派、水質感測器、抽水馬達 進行水質淨化的模擬

## 需要的元件
- <a href='https://zh.m.wikipedia.org/zh-tw/%E6%A0%91%E8%8E%93%E6%B4%BE'>樹莓派</a>
- <a href='https://www.taiwaniot.com.tw/product/grove-turbidity-sensor-meter-%e6%b0%b4%e6%bf%81%e5%ba%a6%e6%84%9f%e6%b8%ac%e5%99%a8-for-arduino-%e6%b0%b4%e8%b3%aa%e6%aa%a2%e6%b8%ac-%e9%a4%8a%e6%ae%96%e7%92%b0%e5%a2%83%e7%9b%a3%e6%b8%ac-seeed/'>Turbidity Sensor (Meter) 水濁度感測器</a>
- <a href='https://www.taiwaniot.com.tw/product/%e5%be%ae%e5%9e%8b-%e6%8a%bd%e6%b0%b4%e9%a6%ac%e9%81%94-%e6%b2%89%e6%b0%b4%e9%a6%ac%e9%81%94-dc3vdc5v/'>微型 抽水馬達 沈水馬達 DC3V~DC5V</a>
- PCF8591模塊 AD/DA轉換模組  https://shopee.tw/PCF8591%E6%A8%A1%E5%A1%8A-AD-DA%E8%BD%89%E6%8F%9B%E6%A8%A1%E7%B5%84-1308-%E5%A4%A7%E6%B4%8B%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90-i.26482219.1624319825

## 實驗所需元件開箱
<img width="1923" alt="Screen Shot 2022-09-08 at 10 57 50 PM" src="https://user-images.githubusercontent.com/21301096/189155908-4ce8d5fd-4bdb-4c5f-b798-28a15e2f1056.png"><br/>

## 樹莓派腳位圖
<img width="1935" alt="Screen Shot 2022-09-08 at 10 58 32 PM" src="https://user-images.githubusercontent.com/21301096/189156176-c21a800b-1260-4646-aca9-27cc95e0ac5a.png">

## 實驗元件接線圖
<img width="2078" alt="Screen Shot 2022-09-08 at 10 58 53 PM" src="https://user-images.githubusercontent.com/21301096/189156205-3b77ce48-035d-499d-87a7-61807fe90a7b.png">

## 設定 I2C 以讀取水質偵測器資訊

- 為了要讓 樹莓派 可以讀到從 水質感應器 上傳入的資料，需要開啟 I<sup>2</sup>C 及SPI的介面

![Screen Shot 2022-09-08 at 11 14 14 PM](https://user-images.githubusercontent.com/21301096/189159787-0f697d7d-4649-4b76-8232-6848a062332a.png)

## 安裝 python-smbus 與  RPi.GPIO 套件

- 在樹莓派的終端機裡使用 `sudo apt install python3-pip` 安裝 Python的 pip 套件管理程式
- 接著使用  `pip3 install RPi.GPIO` 安裝 在 Python 裡的 RPi.GPIO 套件
- 最後使用  `pip3 install smbus` 安裝 在 Python 裡要用到的 smbus 套件

## Reference
1. <a href='https://www.chipwaygo.com/doc/gpio_pin.php'>GPIO簡介</a>
2. <a href='https://www.instructables.com/Water-Quality-Sensor/'>Water Quality Sensor</a>
3. <a href='https://www.electroschematics.com/diy-water-quality-meter-using-a-turbidity-sensor/'>DIY Water Quality Meter Using a Turbidity Sensor</a>
4. <a href='https://wiki.dfrobot.com/Sensor_connection_to_Raspberry_Pi'>Sensor connection to Raspberry Pi</a>
5. <a href='https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html'>Raspberry Pi GPIO Pinout: What Each Pin Does on Pi 4, Earlier Models</a>
6. <a href='https://www.electroniclinic.com/turbidity-sensor-with-arduino-for-water-quality-monitoring-turbidity-meter/'>Turbidity Sensor with Arduino for Water quality monitoring, Turbidity Meter</a>
7. <a href='https://how2electronics.com/diy-turbidity-meter-using-turbidity-sensor-arduino/'>DIY Turbidity Meter using Turbidity Sensor & Arduino</a>
8. <a href='https://www.waveshare.com/wiki/Raspberry_Pi_Tutorial_Series:_PCF8591_AD/DA'>Raspberry Pi Tutorial Series: PCF8591 AD/DA</a>

