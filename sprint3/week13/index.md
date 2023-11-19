---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 13

**Schedule**
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
- Review Sonar.py 
  - GPIO numbers required. Pin numbers did not work
  - GPIO.BCM mode instead of GPIO.BOARD
- Revise all classes to include additional optional parameter.
    - ..., pin_mode:int=GPIO.BOARD):
    - GPIO.setmode(pin_mode)
    - Sonar is exception - pin_mode = GPIO.BCM
    - test all
- Create Rover class
- Create Rover factory
  - [RoverPins.py](RoverPins.py){:target='_blank'}
- Rover testing
  - test all on your own


**Session 2**
    - No class - *Happy Thanksgiving!*
    
---

### Assignments

- Submit weekFinal.zip
  - weekFinal 
    - *model* 
      - rover_factory.py added
      - Rover.py added
      - RoverPins.py added
    - *tests* subfolder.
    - test_rover1.py (test all - final assessment next week)
  - PE1: Mod4 test screen capture included in zip
  