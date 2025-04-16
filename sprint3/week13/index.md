---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 13

**Schedule**
  - Week 13 
    - Review/complete Factory and RoverPins implementation
    - Rover Pins, Rover Factory testing
    - Final Assessment
    - Session 2 - Bluetooth intro/demo
  - Week 14  
    - PE: Summary Test due
    - PE Review
    - Final Project:Coding review
    - Rover app
    - Final Project:Video assigned
  - Week 15 
    - Final Project:Code/Video due - No class, submit by end of day
    - PE1: Certification - No class, submit cert test results by end of the day
    

**Session 1**
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
  wget https://k2controls.github.io/piRover02/sprint3/week13/RoverPins.py  
  ```
  
  - **Rover and rover_factory testing**
    - test_rover1.py
  
**Session 2**

- Review weekFinal including Rover class and Rover Factory module

  - [RAM205 Final Assessment](RAM205_P03_FinalAssessment.pdf){:target='_blank'}
    - [p03_test_rover.py](p03_test_rover.py){:target='_blank'}

```console
wget https://k2controls.github.io/piRover02/sprint3/week13/p03_test_rover.py
```

- Bluetooth services - an intro/instructor demo
  - [Sample Messages](Bluetooth/sample_messages.md){:target='_blank'}
  - [Bluetooth Command Service](Bluetooth/BTCommandService.md){:target='_blank'}
  - [Bluetooth Commands](Bluetooth/BTCommands.md){:target='_blank'}

 
---

### Assignments

- Final Assessment
  - Zip entire weekFinal project including completed p03_test_rover.py
  - Your structure must include model and tests directories.
  - Submit to the Moodle link provided.
  - This is a final assessment. No late work is accepted.
  - Bluetooth functionality is continued next week.
  