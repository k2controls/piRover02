---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 12

**Schedule**
- Schedule
  - Week 12 (this week)
    - PE Mod4 Quiz and Test due
    - weekFinal configuration
    - Ping/sonar sensor
    - Rover Pins, Rover Factory testing
  - Week 13 - Summary Test/Review
    - Rover Pins, Rover Factory testing
    - Bluetooth service
    - Bluetooth testing
    - Bluetooth integration
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
- P02 Review
- PE Mod4 Review
- Final Project configuration
  - Add tests folder to *weekFinal*
    - model
    - tests
  - move all test_.py files to tests folder
  - Modify all test_.py file to include sys.path.append
    - import sys
    - sys.path.append("/home/pi/RAM205/weekFinal/model")
    - Test all to validate
- Sonar class
  - [Event detection and callbacks](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/){:target="_blank"}
  - Event demo - switch_event

**Session 2**
- Drive code - review and complete next week.
- Sonar class
  - [Event detection and callbacks](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/){:target="_blank"}
  - Event demo - switch_event
  - [Ping sensor](https://onlinesrs.co/product/ultrasonic-wave-detector-ranging-module-hc-sr04-hc-sr04-hcsr04-distance-sensor/){:target="_blank"}
  - Sonar class - pins vs GPIO
  - Review GPIO.getmode() and GPIO.setmode() 
  - Existing class work with GPIO.BCM setting?
  
- Rover class and Rover Factory
  - Create Rover class
  - Create Rover factory
    - [RoverPins.py](RoverPins.py){:target='_blank'}
- Rover testing

### Assignments

- PE1: Mod 4 Quiz and Test
- weekFinal.zip (verify all test function)
  - Rover
    - Buzzer.py
    - Drive.py
    - Gimbal.py
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
