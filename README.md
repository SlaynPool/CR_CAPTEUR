---
author:
- Nicolas Vadkerti
title: Le Protocole MQTT
---

<https://github.com/SlaynPool/CR_CAPTEUR/>

Reinstallation du PI et de la maquette MQTT
===========================================

Pour installer le PI, il suffit d'utiliser dd:

-   ``` {#commande/1.txt .default caption="Installation de raspian" label="commande/1.txt" style="Style1"}
    unzip -p 2019-09-26-raspbian-buster-lite.zip |sudo dd  of=/dev/sdd bs=2M && sync 

    ```

Pour le déploiment de la maquette:\
<https://github.com/SlaynPool/CR_MQTT/>

Utilisation et découverte du Hat 
=================================

Pour l'utilisation et la mise en place du Sense Hat, on peut utiliser la
librairie Python :

-   ``` {#commande/2.txt .default caption="Mise en place du hat" label="commande/2.txt" style="Style1"}
    sudo apt-get update
    sudo apt-get install sense-hat
    sudo pip-3.2 install pillow
    ```

Pour experimenter avec le hat, j'ai ecris des bouts de codes, avec des
utiliter discutables:

-   ``` {#src/prog1.py .python caption="Premier Programme" label="src/prog1.py" style="Style1"}
    from sense_hat import SenseHat

    sense= SenseHat()
    sense.clear()

    while True:
        sense.set_pixel(3,0, 0,255,0)
        sense.set_pixel(4,0, 0,255,0)
        sense.set_pixel(2,1, 0,255,0)
        sense.set_pixel(5,1, 0,255,0) 
        sense.set_pixel(2,2, 0,255,0)
        sense.set_pixel(5,2, 0,255,0)
        sense.set_pixel(2,3, 0,255,0)
        sense.set_pixel(5,3, 0,255,0)
        sense.set_pixel(1,4, 0,255,0)
        sense.set_pixel(2,4, 0,255,0)
        sense.set_pixel(5,4, 0,255,0)
        sense.set_pixel(6,4, 0,255,0)
        sense.set_pixel(0,5, 0,255,0)
        sense.set_pixel(7,5, 0,255,0)
        sense.set_pixel(0,6, 0,255,0)
        sense.set_pixel(7,6, 0,255,0)
        sense.set_pixel(1,7, 0,255,0)
        sense.set_pixel(2,7, 0,255,0)
        sense.set_pixel(5,7, 0,255,0)
        sense.set_pixel(6,7, 0,255,0)

        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        print(pressure)
    ```

Ce programme dessine un dessin en vert sur la matrice de pixel du hat et
affiche sur le STDOUT la valeur du capteur de pression.

Envoi des relevés via MQTT
==========================

Pour faire ca en python, on va utiliser la bibliotèque PAHO MQTT. Et
j'ai donc ecris ceci pour envoyer les informations de l'accelerometres
en MQTT:

-   ``` {#src/monProg.py .python caption="Mon petit programme" label="src/monProg.py" style="Style1"}
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
         
    ```

Comme notre telegraf est bien configuré, on peut visualiser nos données
sur grafana.

![visualiser[]{label="fig:qos"}](img/grafana.jpg){#fig:qos}

On recupère correctement les Informations de temperature, et des 3 axes
de l'accelerometres mesuré par le hat.
