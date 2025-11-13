---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 12

**Schedule**
- Week 12 
  - PE Mod4 Test due
  - Review Servo - add update() - set position
  - Create gimbal container
    - left(), right() up(), down(), center(), update()
  - Add Drive class with testing 
  - Ping/sonar sensor added
- Week 13 
  - PE: Summary Test assigned
  - Rover Pins, Rover Factory testing
  - Bluetooth service
  - Bluetooth testing
  - Bluetooth integration
- Week 14  
  - Session 1
    - PE: Summary Test due
    - P03 Part 1 Assigned
  - Session 2
    - None - Thanksgiving break
- Week 15
  - P03 Part 1 review
  - PE Review
  - PE Exam setup
  - Smartphone app intro
  - P03 part 2 assigned
- Week 16 
  - Session 1: Final Project:
    - Video due - submit by end of day
    - No Zoom class but Keith is available
  - PE1: Certification 
    - Complete and post cert results by the end of the day.
    - No class  

**Session 1**

- Week 11 review
  - Final project configuration (See Assignment section below)
    - *weekFinal*
      - *model*
      - *tests*
- **Servo class**
  - constructor, deconstructor
  - cw(), ccw(), center()
  - update(position) with position normalized between 0 and 1

- **Gimbal class**
  - Basic interface defined during class up, down, left, right, center(), and update().
  - *Implementation and testing (test_gimbal) on your own.*  
  - See RGB_LED for similar structure and testing.
  - Extend to include gimbal.update() function enabling partial motion.
    
- add **Drive class** 
  - Drive.py
    - constructor
    - deconstructor
    - update() function
      - Operation
      - Speed adjust
    

  
**Session 2**

- Drive
  - Speed control
    - Speed up, Speed down
    - set_speed
  - Extend update()
    - update(self, operation:Operation=None, speed:int=None, change_speed:int=0):
  - test speed and update functionality
       
- Sonar class 
  - [Event detection and callbacks](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/){:target="_blank"}
  - Event demo - switch_event  
  - [add_event_detect issue!](event_detect_issue.md){:target="_blank"}
  - [Ping sensor](https://onlinesrs.co/product/ultrasonic-wave-detector-ranging-module-hc-sr04-hc-sr04-hcsr04-distance-sensor/){:target="_blank"}
  - sonar.distance vs. sonar.get_distance()
  
- Refactoring class for GPIO
  - Sonar class - pins vs GPIO
  - Review GPIO.getmode() and GPIO.setmode() 
  - Existing classes do not work with GPIO.BCM setting. GPIO.BOARD is hardcoded.
  - Refactor all classes using the following (except Sonar). This enables GPIO mode to be set globally.

```Python
        if GPIO.getmode() == None:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
```
  
- Rover class and Rover Factory
  - Create Rover class
  - Create Rover factory
    - [RoverPins.py](RoverPins.py){:target='_blank'}

```Console
wget https://k2controls.github.io/piRover02/sprint3/week12/RoverPins.py  
```

### Assignments

- PE1: Mod 4 Test
- weekFinal.zip (Verify all test functions. Zip project with structure.)
  - model
    - Buzzer.py
    - Drive.py  
    - LED.py
    - RGB_LED.py
    - Servo.py
    - Sonar.py  
    - Warner.py
  - tests
    - test_buzzer.py
    - test_drive.py 
    - test_led.py
    - test_rgb.py
    - test_servo.py
    - test_sonar.py 
    - test_warner.py       
