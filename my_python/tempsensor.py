import time
import board
import adafruit_dht

dhtDevice=adafruit_dht.DHT11(board.P8_11)
while True:
    try:
        temp_c = dhtDevice.temperature
        temp_f = temp_c *(9/5)+32
        humidity=dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temp_f,temp_c,humidity))

    except:
        print(error.args[0])

    time.sleep(2.0)



