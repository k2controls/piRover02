---
layout: default
---

# RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 2](../) - Week 09


**Session 1**

- Introduction to Python classes
- AI Prompt: What is the advantage of using classes when programming in Python?
 
- Dog class
- Here's a great reference with even more on a Dog class example.
    - [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/){:target="_blank"}
- LED class - interface planning
    - Review your RAM155 piRover solution (~/piRover/workingP03)
    - Locate your piRover_led.py module
    - Identify the properties and methods for a single LED
    - Edit [this text document](LED.txt){:target="_blank"} and list.
    - Are there other methods that we should include in our class?
    - Be sure to include any required or optional parameters when defining LED methods.

**Session 2**

- PE1: Module 3 Coding - part 2 (bitwise and data structures)
- piRover classes - continued
  - LED as a class
    - review LED plan
      - __init__()
      - on()
      - off()
      - toggle()
      - blink()
      - dim()
    - review the use of self param. What others are required?
    - review __init__ parameters
    - consider the structure used for PWM in Week 6 warner
    - revise __init__() to create a PWM port. Be sure to use the self reference.
    - use your class's PWM reference to implement on(), off(), toggle(), blink(), and dim().
    - How can you use the optional active_low parameter to invert the PWM pulse?
  - deconstructor/cleanup()?
- RGB_LED as a class - RGB_LED.py
  - navigation
  - set_color() 
  - rgb_led_test.py 

  
---

### Assignments

- PE1: Mod 3 Test
- LED.py 
- test_led.py
- RGB_LED.py
- test_rgb_led.py


