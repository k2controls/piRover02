---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 1](../) - Week 04 

**Announcements**
1. Week 05 Session 1 (next week): Research on your own with report out during Session 2. See link below for Research document. Submit your work by end of Session 1 day. Class report out is at session 2.
2. We're looking to hire new NMC Makerspace lab technicians this semester. You'll need to be enrolled at NMC at least through next school year. Email me if you are interested.

**Session 1**
- PE1: Mod 1 Test - Questions?
 
- Rover Mods for Week04
  - Breadboard
  - Amber LED and hardware
  - MOSFET module and hardwar
  - M-F Servo cable with shield remmove (headers position 4 to breadboard)
  - F-F Servo cable (header position 5 to MOSFET module)
  - JST connector to MOSFET Vin,GND
  - Amber LED to MOSFET V+,V-

- Digital Outputs
  - Switching - high side vs low side 
    - AI Prompt - "I'm learning how to interface electronic control circuits to microcontroller outputs. I'm specifically working on a Raspberry Pi. I'm trying to understand high-side versus low-side switching and when I should be activating an output circuit with a logic high from an output port versus and logic low fron an output port. First, please explain high-side vs low-side using basic switches."
    - AI Prompt = "Can you locate a schematic diagram that uses switches to explain high-side and low-side?"
    - [High Side and Low Side Switches](https://www.rohm.com/electronics-basics/ipds/high-side-and-low-side-drive){:target="_blank"}

- [RAM205.DigitalOutputs](RAM205.DigitalOutputs.docx)
 
**Session 2**
 
- [Digital Outputs](RAM205.DigitalOutputs.docx) (con't)
      - Low-side switch of LED issue with +5V source
      - Use of BJT transistor to resolve
      - 74__244 line driver to resolve
      - Voltage divider solution

- [Digital Outputs - Driving high current loads](../week05/RAM205.DrivingHighCurrentLoads.pdf){:target="_blank"} (intro) 

- Week 5 Session 1 - research project - on your own
  - [Power and Control Research Activity](../week05/RAM205.PowerAndControlResearch.docx)

---

### Assignments

- Digital Outputs 
  - Submit .docx or .pdf file with measurements and detailed summary.
    - See instructions for summary. 
    - Detailed response is required. 
    - Discuss high-side and low-side configurations and constraints when driving loads using a GPIO port. 
    - Discuss any issues with the procedures.
  - Digital Output - video lab check
    - Submit video. Be sure to show resistor configuration on breadboard.
- Digital Outputs - Driving high current loads - video lab check
  - Submit video of Amber blink

