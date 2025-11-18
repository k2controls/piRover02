---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 13

**Schedule**
- Week 13 
  - Session 1
    - PE: Summary Test assigned
    - Ping/Sonar class - testing and revision
    - Rover Pins, Rover Factory testing
  - Session 2
    - Rover Factory - Review
    - Bluetooth service - introduction *(P03 Part 2 content)*
    - P03 Part 1 Assigned
- Week 14  
  - Session 1
    - *P03 Working - No Zoom session, KEK online*
    - **PE: Summary Test Due** - end of the day, *Wednesday, Nov 26*
    - **P03 Part 1 Due** - end of the day, *Wednesday, Nov 26*
  - Session 2
    - *None - Thanksgiving break*
- Week 15
  - Session 1
    - P03 Part 1 review
    - PE Review
    - Bluetooth service - setup and integration
  - Session 2  
    - PE Exam setup
    - Smartphone app intro
    - P03 Part 2 assigned
- Week 16 
  - Session 1: Final Project:
    - **P03 Part 2 Video due** - submit by end of day
    - No Zoom class but Keith is available
  - Session 2: **PE1: Certification** 
    - Complete and post cert results by the end of the day.
    - No class  

**Session 1**

  - [Expansion Board Manual](https://k2controls.github.io/piRover02/hardware_kit/expansionBoardManual.pdf){:target='_blank'}

  - REVIEW: Refactoring classes for GPIO
    - Sonar class - pins vs GPIO
    - Review GPIO.getmode() and GPIO.setmode() 
    - Existing classes did not work with GPIO.BCM setting. 
      - GPIO.BOARD is hardcoded.
    - Refactor _all_ classes using the following (except Sonar). This enables GPIO mode to be set globally.
  
  ```Python
          if GPIO.getmode() == None:  # if mode is not set then Pins
              GPIO.setwarnings(False)
              GPIO.setmode(GPIO.BOARD)
  ```
    
  - Rover class and Rover Factory
    - Create Rover class
    - Create Rover factory
      - [RoverPins.py](RoverPins.py){:target='_blank'}
  
  ```Console
  wget https://k2controls.github.io/piRover02/sp3/w13/RoverPins.py  
  ```
  
  - **Rover and rover_factory testing**
    - test_rover1.py
  
**Session 2**

<!-- - Review weekFinal including Rover class and Rover Factory module

- [RAM205 Final Assessment](RAM205_P03_FinalAssessment.pdf){:target='_blank'}
  - [p03_test_rover.py](p03_test_rover.py){:target='_blank'}

```console
wget https://k2controls.github.io/piRover02/sprint3/week13/p03_test_rover.py
```

- Bluetooth services - an intro/instructor demo
  - [Sample Messages](Bluetooth/sample_messages.md){:target='_blank'}
  - [Bluetooth Command Service](Bluetooth/BTCommandService.md){:target='_blank'}
  - [Bluetooth Commands](Bluetooth/BTCommands.md){:target='_blank'} -->

 
---

### Assignments

- None, but review next week's schedule. Practice zipping the entire weekFinal solution. Open your resulting zip file and verify you have the required content included. This is a final course assessment. Do your own work and be sure you are submitting all requirements as a zip file to next week's link. 
  