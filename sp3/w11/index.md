---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 2](../) - Week 11

- PE: Module 4 Quiz due
- Schedule
  - Week 11 (this week)
    - Session 1
      - P02 assessement
    - Session 2  
      - weekFinal configuration
        - LED, RGB_LED, Buzzer, and Warner to model directory
        - all test_.py files to tests directory
      - Add Servo and Gimbal with testing
- Week 12 
    - PE Mod4 Test due
    - Add Drive class with testing 
    - Ping/sonar sensor added
- Week 13 - Summary Test/Review
  - Rover Pins, Rover Factory testing
  - Bluetooth service
  - Bluetooth testing
  - Bluetooth integration
- Week 14  
  - Session 1
    - PE: Summary Test due
    - PE Review
    - P03 Part 1 Assigned
  - Session 2
    - None - Thanksgiving break
- Week 15
  - P03 Part1 review
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
- PO2 Sprint 2 Assessment

**Session 2**
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

- Gimbal class - container with two servos
      
---

### Assignments

- PE1: Mod 4 Quiz
- weekFinal.zip 
  - includes all weekFinal with folder structure in zip.
    - model subfolder
      - Buzzer.py
      - LED.py
      - RGB_LED.py
      - Servo.py
      - Warner.py
    - tests subfolder
      - test_buzzer.py
      - test_led.py
      - test_rgb_led.py
      - test_servo.py
      - test_warner.py
  - all test_.py refactor with sys.path.append in tests folders.
    - *All tests must run with no errors in class file.
  
  
