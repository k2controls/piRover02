---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 12


**Schedule**
- Week 12 (this week)
  - PE Mod4 Quiz
  - P02 test review
  - PE Mod4 Review
  - weekFinal solution structure
  - Sonar
- Week 13 
  - PE Mod4 Test
  - S1 - Rover Pins, Rover Factory testing
  - S2 - holiday break
- Week 14
  - Bluetooth service
  - Bluetooth testing
  - Final Project/Coding due
- Week 15
  - PE: Summary Test due
  - PE Review
  - Final Project/Coding review
  - Rover app
  - Final Project/Video assigned
    - Final project test code
    - Rover App
- Week 16
  - Final Video due - No class, submit by end of day
  - PE1: Certification - No class
    
**Session 1**
- P02 Review
- PE Mod4 Review
- Final Project configuration
  - Add tests folder to weekFinal
    - model
    - tests
  - move all test_.py files to tests folder
  - Modify all test_.py file to include sys.path.append
    - import sys
    - sys.path.append("/home/pi/RAM205/weekFinal/model")
    - Test all to validate

**Session 2**
- Sonar class
  - [Event detection and callbacks](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/){:target="_blank"}
  - Event demo - switch_event
  - [Ping sensor](https://onlinesrs.co/product/ultrasonic-wave-detector-ranging-module-hc-sr04-hc-sr04-hcsr04-distance-sensor/){:target="_blank"}
  - Sonar class - pins vs GPIO

### Assignments

- PE1: Mod 4 Quiz
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
