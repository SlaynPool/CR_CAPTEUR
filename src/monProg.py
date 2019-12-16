from sense_hat import SenseHat
import paho.mqtt.client as mqtt
mqttc = mqtt.Client("PI")
mqttc.connect("10.202.0.92")
mqttc.loop_start()


import time

mqttc.publish("sensor/temperature", payload="test", qos=0, retain=False)


sense= SenseHat()
sense.clear()

while True:
     #Dessin de base:
     sense.set_pixel(1,7, 0,255,0)
     sense.set_pixel(2,7, 0,255,0)
     sense.set_pixel(4,7, 0,255,0)
     sense.set_pixel(5,7, 0,255,0)
     sense.set_pixel(1,6, 0,255,0)
     sense.set_pixel(2,6, 0,255,0)
     sense.set_pixel(4,6, 0,255,0)
     sense.set_pixel(5,6, 0,255,0)
     sense.set_pixel(3,5, 0,255,0)
     sense.set_pixel(3,6, 0,255,0)
     sense.set_pixel(3,4, 0,255,0)


#On recupere des capteurs en tous genre
     accel_only = sense.get_accelerometer()
     roll= round(accel_only["roll"],1)
     pitch= round(accel_only["pitch"],1)
     yaw= round(accel_only["yaw"],1)
     
     temp = sense.get_temperature()


     
     mqttc.publish("sensor/temperature", payload=temp, qos=0, retain=False)
     mqttc.publish("sensor/accelero/roll", payload=roll, qos=0, retain=False)
     mqttc.publish("sensor/accelero/pitch", payload=pitch, qos=0, retain=False)
     mqttc.publish("sensor/accelero/yaw", payload=yaw, qos=0, retain=False)
     


     
     time.sleep(1) 
     sense.clear()
     print(roll)
     

