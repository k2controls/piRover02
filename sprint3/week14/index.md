---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 14

**Schedule**
  - Week 14  
    - PE: Summary Test due - See Moodle link
    - Session 1 - PE Review
    - Session 2 - PE Review - slicing and exceptions
    - Final Project:Coding review
    - Rover app
    - Final Project:Video assigned
  - Week 15 
    - Final Project:Code/Video due - No class, submit by end of day
    - PE1: Certification - No class, submit cert test results by end of the day

**Session 1**
  - Session 2 >> Final Assessment review - p03_test_rover.py
  - PE Review - PE_review.py

  - Smartphone app - initial
    - Add the following to your Model directory  
      - [Bluetooth Command Service](Bluetooth/BTCommandService.py){:target='_blank'}
      - [Bluetooth Commands](Bluetooth/BTCommands.py){:target='_blank'}
      
      ```
      wget https://k2controls.github.io/piRover02/sprint3/week14/Bluetooth/BTCommands.py
      wget https://k2controls.github.io/piRover02/sprint3/week14/Bluetooth/BTCommandService.py
      ```
    - Bluetooth testing
    
**Session 2**

- Python Certification Test 
  - [Preparation/Process](cert_test_directions/index.md)
    - Voucher Numbers - See PE: Certification assign link. Open to view comment. Copy voucher number.
    - Do system check prior to exam time. Use NMC workstation if in doubt.
    - Deadline to post PE Certification image is next Week 15 Session 2.

- PE Review
  - slicing
  - exceptions

- P03 part 1 review
  - Final Assessment review - p03_test_rover.py
    - rover.rgb_led
    - other?

```python
  # use patterns to create rgb object
  # TODO
  r1 = LED(RoverPins.LED_RED_PIN)
  g1 = LED(RoverPins.LED_GREEN_PIN)
  b1 = LED(RoverPins.LED_BLUE_PIN)

  my_rgb_led = RGB_LED(r1, g1, b1)
  rover.rgb_led = my_rgb_led
```


- Smartphone app 
  - app_smartphone.py




---

### Assignments

- PE Summary Test

