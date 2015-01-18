# Agobo
Python files for my robot Hugo "Agobo". The Agobo is a Raspberry Pi A+ based robot
![alt](http://4tronix.co.uk/blog/wp-content/uploads/2014/11/abp02.jpg)

##maze_solver.py

This is a test script that uses the ultrasonic sensor at the front of the robot to "see" the world around it. The robot is programmed so that it always goes forward, but if an obstacle gets within 20cm then it will turn 90 degrees right and search for an escape.

