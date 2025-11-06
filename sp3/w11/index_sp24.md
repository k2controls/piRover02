---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 2](../) - Week 11

- PE: Module 4 Quiz due
- Schedule
  - Week 11 (this week)
    - weekFinal configuration
      - LED, RGB_LED, Buzzer, and Warner to model directory
      - all test_.py files to tests directory
      - Add Servo and Gimbal with testing
      - Add Drive class with testing 
- Week 12 
    - PE Mod4 Test due
    - Ping/sonar sensor added
    - Rover Pins, Rover Factory introduction
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

- **Final Project configuration**
  - Add tests folder to *weekFinal*
    - model
    - tests
  - move all test_.py files to tests folder
  - Modify all test_.py file to include sys.path.append
    - import sys
    - sys.path.append("/home/pi/RAM205/weekFinal/model")
    - Test all to validate

**Servo and Gimbal**
- Servo as a class
  - [RAM155 Servo project](P03.RemoteDrive.Servo.pdf){:target="_blank"}
    - [piRover_servo.py](piRover_servo.py){:target="_blank"}
  - Create Servo.py
    - Servo update() - normalized position parameter

```python
  def update(self, position:float):
      # 0 pos is ccw and 1 is cw
      if position < 0 or position > 1:
          print("Invalid  position value")
      else:
          dc_range = self.ccw_dc - self.cw_dc
          dc_setpoint = dc_range * position
          dc_value = self.ccw_dc - dc_setpoint
          self.pwm.ChangeDutyCycle(dc_value)

```


**Session 2**

- Servo class review
  - update() vs set_position()
  - Required pins for Gimbal servos - HEADER_1 and HEADER_2
  
- Gimbal class
  - Instructor will define required interface
  - complete Gimbal class on your own
  - complete test_gimbal on your own.

- **Drive Class with testing**
  - Parameters for drive constructor?
  - Change direction
  - Change speed
  - increment/decrement speed
      
---

### Assignments

- PE1: Mod 4 Quiz
- weekFinal.zip 
  - includes all weekFinal with folder structure in zip.
    - model subfolder
      - Buzzer.py
      - Drive.py
      - **Gimbal.py** *- implement on your own*
      - LED.py
      - RGB_LED.py
      - Servo.py
      - Warner.py
    - tests subfolder
      - test_buzzer.py
      - **test_drive.py** *- additional testing required*
      - **test_gimbal.py** *- create,test - adjust params as required*
      - test_led.py
      - test_rgb_led.py
      - test_servo.py
      - test_warner.py
  - all test_.py refactor with sys.path.append in tests folders.
    - *All tests must run with no errors in class file.
  
  
