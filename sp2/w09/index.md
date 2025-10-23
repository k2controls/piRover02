---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 2](../) - Week 09 

**Session 1**

- PE Module 3 - Quiz due
- PE Module 3 - Test due

- [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/){:target="_blank"}

- Dog class - an example

- RAM 155 examples
  - PWM (servo)
  - Bluetooth

- LED class - interface planning
    - Review your RAM155 piRover solution (~/piRover/workingP03)
    - Locate your piRover_led.py module
    - Identify the properties and methods for a single LED
    - Edit [this text document](LED.txt){:target="_blank"} and list.
    - Are there other methods that we should include in our class?
    - Be sure to include any required or optional parameters when defining LED methods.

- LED() class with demo

**Session 2**

- PE Module 3 review - part 2
  - Data collections: tuple, list, dictionary

- piRover classes - continued
  - LED as a class
    - review LED plan
      - \__init__()
      - on()
      - off()
      - toggle()
      - blink()
      - dim()
    - review the use of self param. What others are required?
    - review \__init__ parameters
    - consider the structure used for PWM in Week 6 warner
    - As a class
      - revise \__init__() to create a PWM port. Be sure to use the self reference.
      - use your class's PWM reference to implement on(), off(), toggle(), blink(), and dim().
      - How can you use the optional active_low parameter to invert the PWM pulse?
      - how is toggle() implemented? Can you create as is_on() method? How did you define?
    - deconstructor/cleanup()?

- RGB_LED as a class - RGB_LED.py
  - navigation
  - set_color()
  - - test_led.py - tests for LED and RGBLed classes

---

### Assignments
- PE1: Module 3 Quiz
- PE1: Module 3 Test
- Dog.py - Dog as a class
- test_dog.py - tests for Dog class
- LED.py - LED as a class
- test_led.py - tests for LED class
- RGBLed.py - RGB LED as a class using LED class
- test_led.py - tests for RGBLed class




  
