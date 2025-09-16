---
layout: default
---

## RAM 205 - Robotics and Automation

### [RAM205](../../) - [Sprint 1](../) - Week 04 

**Announcements**
1. Week 05 preview (next week): Research on your own with report out to the class. See link below for Research document. 
- Week 5 Session 2 - research project - on your own
  - [Power and Control Research Activity](../week05/RAM205.PowerAndControlResearch.docx)

-<video controls src="../week05/RAM205ResearchProjectOverview.mp4" title="Power and Control Research Activity"></video>

**Session 1**
- PE1: Mod 1 Test - Questions?
 
- Rover Mods - assigned last week
  - Breadboard
  - Amber LED and hardware
  - MOSFET module and hardware
  - M-F Servo cable with shield removed (headers position 4 to breadboard)
  - F-F Servo cable (header position 5 to MOSFET module)
  - JST connector to MOSFET Vin,GND
  - Amber LED to MOSFET V+,V-
  - See session video for instructor demo

- DC Power Sources - The Yahboom G1 Tank example
    - Review: [Voltage regulation](https://youtu.be/D52xUrIDrZY){:target="_blank"}
    - Raspberry PI power supply
      - [Expansion board manual](../../hardware_kit/expansionBoardManual.pdf) 
      - [Yahboom G1 Control Board Schematic](yahboom_G1_schematic.pdf){:target="_blank"}
      - Battery connection S3 and S4
      - VM
      - VCC
      - U10 3.3V
      - MVCC - 3.3V/5V

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


---

### Assignments
1. Digital Outputs 
  - Submit .docx or .pdf file with measurements and detailed summary.
    - See instructions for summary. 
    - Detailed response is required in final summary prompt. 
    - Discuss high-side and low-side configurations and constraints when driving loads using a GPIO port. 
    - Discuss any issues with the procedures.
3. Digital Output 1 - Lab Check
  - Completed during class?
  - If not, include short video.
  - Be sure to show resistor configuration on breadboard.
3. Digital Output 2 - Lab Check - Next week?
  - Next week?
  - Amber LED blink with MOSFET driver
