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

