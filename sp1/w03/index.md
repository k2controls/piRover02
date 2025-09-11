---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 1](../) - Week 3 

**Session 1**
- PE Module 1 Test due
  - PE Module 1 review
- Continued: [Power Sources](../week02/RAM205.PowerSources.pdf){:target="_blank"}
    - *Week 4 Assignent:* Internal Resistance of a Power Source - Video presentation
    - See requirements in *Assignments* below and related rubric.
- Today's procedure
  - Power Sources - Test 1 review. Add drive test
    - drive code - created last week. 
    - .config/autostart issues?
  - Test 1 - check values with Pi as load. 
  - Test 2 - drive as load
  - Continue with Test 3 - AC power source with drive as load
  
- Power Supply Test Data (posted later)
  - [Class Data Set](power_supply_class_data.pdf){:target="_blank"}
  
- Review of class data and conclusions
- Power Supply video report-out due next week - 50 points, See rubric/grading below
  - [Power Supply Video Rubric](eval.md){:target="_blank"} 


**Session 2**

- Rover Mods for Week04
  - Breadboard
  - Amber LED and hardware
  - MOSFET module and hardware
  - M-F Servo cable with shield removed (headers position 4 to breadboard)
  - F-F Servo cable (header position 5 to MOSFET module)
  - JST connector to MOSFET Vin,GND
  - Amber LED to MOSFET V+,V-
  - See session video for instructor demo

- Digital Outputs
  - Switching - high side vs low side 
    - AI Prompt - "I'm learning how to interface electronic control circuits to microcontroller outputs. I'm specifically working on a Raspberry Pi. I'm trying to understand high-side versus low-side switching and when I should be activating an output circuit with a logic high from an output port versus and logic low fron an output port. First, please explain high-side vs low-side using basic switches."
    - AI Prompt = "Can you locate a schematic diagram that uses switches to explain high-side and low-side?"
    - [High Side and Low Side Switches](https://www.rohm.com/electronics-basics/ipds/high-side-and-low-side-drive){:target="_blank"}

- Week 04 preview - [RAM205.DigitalOutputs](RAM205.DigitalOutputs.pdf)

---

### Assignments

- PE1: Module 1 Test
  - screen capture included showing score
  - Test scores are recorded
- Video presentation (50 points)
  - The use of Zoom video is required so that your computer screen showing diagrams, data, and code can be shared.
  - Create cloud recording and submit Zoom url to assignment link.
  - Requirements: Internal Resistance of a Power Source
    1. Introduction: Introduce the activity including Rs and its relationship to battery quality, capacity, and voltage regulation. (see resources)
    2. Testing Procedure: Discuss testing procedure including details on Test 1, Test 2, and Test 3. How do they relate?
    3. Test setup: include either an image of your test setup or include the test setup as part of your video.
    5. Circuit Analysis: **Share an image of the circuit** showing Rs as a part of a voltage source. Describe how the value of Rs was determined for the **piRover battery**. Discuss terminal voltage, voltage drop, current flow, Ohm's law, KVL, etc.
    5. Summary: Close with a summary of the activity. Discuss class data and compare the results of your battery. What did you learn? 
