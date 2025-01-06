---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 3](../) - Week 14

**Schedule**
  - Week 14  
    - PE: Summary Test due
    - PE Review
    - Final Project:Coding review
    - Rover app with Bluetooth
    - Final Project:Video assigned
  - Week 15 
    - Final Project:Code/Video due - No class, submit by session 1 end of day
    - PE1: Certification - No class - submit by session 2 end of day

**Session 1**
  - Final Assessment review - p03_test_rover.py
  - PE Review - review_cert_review.py

  - Smartphone app - initial
    - Add the following to your Model directory  
      - [Bluetooth Command Service](Bluetooth/BTCommandService.py){:target='_blank'}
      - [Bluetooth Commands](Bluetooth/BTCommands.py){:target='_blank'}
      
      ```
      wget https://k2controls.github.io/piRover02/sprint3/week14/Bluetooth/BTCommands.py
      wget https://k2controls.github.io/piRover02/sprint3/week14/Bluetooth/BTCommandService.py
      ```

**Session 2**

- P03 part 1 review
  - RGB_LED

```python
  # use patterns to create rgb object
  # TODO
  r1 = LED(RoverPins.LED_RED_PIN)
  g1 = LED(RoverPins.LED_GREEN_PIN)
  b1 = LED(RoverPins.LED_BLUE_PIN)

  my_rgb_led = RGB_LED(r1, g1, b1)
  rover.rgb_led = my_rgb_led
```

- BTCommand Service - bug fix

```python
'''
v2.3 - bug fix - mode message missing commandID
4/24/2024
'''
# see line 81
  command.command_id = Messages.BUTTON_MESSAGES[message]
```

- Smartphone app - continued
  - analog messages - use servo slider for speed
  - shut down
  - extension - obstacle detect
- [EnablingAppAtStartup.pdf](EnablingAppAtStartup.pdf){:target='_blank'}

- Python Certification Test 
  - [Preparation/Process](cert_test_directions/index.md)
    - Voucher Numbers - See PE: Certification assign link. Open to view comment. Copy voucher number.
    - Do system check prior to exam time. Use NMC workstation if in doubt.
    - Deadline to post PE Certification image is next Week 15 Session 2.

- PE review
  - exceptions
  - slicing
  
---

### Assignments

- None. Final code and demo due Week 15. See links.

<!--
---

 ### Assignments

- Final Assessment
  - Zip entire weekFinal project including completed p03_test_rover.py
  - Your structure must include model and tests directories.
  - Submit to the Moodle link provided.
  - This is a final assessment. No late work is accepted.
  - Bluetooth functionality is continued next week. -->
  