import agobo, time
speed = 80

agobo.init()

try:
    while True:
        a = agobo.getDistance()
        if a < 20:
        	agobo.spinRight(speed)
        	time.sleep(1)
        elif agobo.getSwitch() == True:
        	agobo.setAllLEDs(1)
        	time.sleep(0.5)
        	agobo.setAllLEDs(0)
        else:
        	agobo.forward(speed)
        	time.sleep(1)
except KeyboardInterrupt:
    print("EXIT")
finally:
    agobo.cleanup()