---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 12

**Schedule**
- Week 12 
  - PE Mod4 Test due
  - Continue Drive class with testing 
  - Ping/sonar sensor added
  - Rover Pins, Rover Factory introduction
- Week 13 - Summary Test/Review
  - Rover Pins, Rover Factory testing
  - Bluetooth service
  - Bluetooth testing
  - Bluetooth integration
  - Final Project/Coding due
- Week 14  
  - PE: Summary Test due
  - PE Review
  - Final Project:Coding review
  - Rover app
  - Final Project:Video assigned
- Week 15 
  - Final Project:Video due - No class, submit by end of day
  - PE1: Certification - No class  

**Session 1**
- Week 11 review
  - Final project configuration (See Assignment section below)
    - *weekFinal*
      - *model*
      - *tests*
  - Servo class
    - constructor, deconstructor
    - cw(), ccw(), center()
    - update(position) with position normalized between 0 and 1
  - Gimbal class
    - Basic interface defined during class up, down, left, and right.
    - Implementation and testing (test_gimbal) on your own.
    - See RGB_LED for similar structure and testing.
    - Extend to include update() type of function enabling partial motion.
    
- PE Mod4 Review
  - Functions and parameters - a review
  - Data collections
    - tuple and list review
    - dictionaries

- Drive code 
  - review Week 11 code
  - Add speed coding
  - Add update()
  - Test
  

  
**Session 2**

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
    - Drive.py  (completed)
    - Gimbal.py
    - LED.py
    - RGB_LED.py
    - Servo.py
    - Sonar.py  (added)
    - Warner.py
  - tests
    - test_buzzer.py
    - test_drive.py (completed)
    - test_led.py
    - test_rgb.py
    - test_servo.py
    - test_sonar.py (added)
    - test_warner.py       
