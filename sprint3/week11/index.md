---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 2](../) - Week 11

**Session 1**

- PE: Module 4 Quiz and Test due next week
- Schedule
  - Week 11 (this week)
    - S1 
      - Drive class review (week 10)
      - Drive class and testing, no code submission required.
    - S2 - P02 Test See below.
  - Week 12
    - PE Mod4 Quiz and Test due
    - Rover Pins, Rover Factory testing
  - Week 13 - Summary Test/Review
    - Bluetooth service
    - Bluetooth testing
    - Final Project:Coding due
  - Week 14  
    - PE: Summary Test due
    - PE Review
    - Final Project:Coding review
    - Rover app
    - Final Project:Video assigned
  - Week 15 
    - Final Project:Video due - No class, submit by end of day
    - PE1: Certification - No class

- Gimbal review
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

- piRover_drive (review from partner coding last week - functional?)
- Drive.py - initial version via Week10 piRover_drive.py
- Drive.py
  - constructor
  - deconstructor
  - update() function
    - Operation
    - Speed adjust
 
**Session 2**

- ## P02 Testing ####
  
<!-- - No class session
  - Complete on your own during class session
  - P02 Testing link open at 10:15 and closes as 12:15
  - Directions are provided as link
  - Submit code to Moodle link prior to session close. -->
       
---

### Assignments

- None other than P02 coding submitted during Session 2
  
