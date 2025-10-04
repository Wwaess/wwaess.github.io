---
title: "Polymorphism for a Humanoid Robot"
date: 2025-08-30 00:00:00 +0000
categories: [OOP]
tags: [OOP]
---

# To clarify - What IS Polymorphism?

Suppose we have two different cars. One has an automatic transmission and the other has a manual transmission. We can drive both of them from parked to 20 mph, but the processes are different. In the automatic you:
- apply the brake 
- switch from the P-gear to the D-gear
- release the brake 
- accelerate to that speed. 

In the manual: 
- engage the clutch
- swtich gears from neutral to first
- release the clutch to its biting point (else you'll slip the clutch and cause a stall)
- accelerate
- re-engage the clutch while releasing the gas pedal to switch up a gear, maybe even twice
- keep accelerating until you reach that speed. 

These are two different methods that achieve the same thing. In object-oriented programming, we can do a similar thing where we define two different functions for two different objects (well, their classes) but call them the same name ("drive_to_20mph" in this case). That way we can invoke both of them with the same name, and the class management will identify _which_ class's function we're referring to. 

Here's an example for my summative assignment where I'm designing a humanoid robot for an instrument assembly workshop:


```py
from time import sleep

class LuthierRobot:
    def __init__(self, name): 
        self.name = name
    
    def service_instrument(self, instrument: Instrument): # reminder - this checks that "instrument" has the class "Instrument"
        print(f"{self.name} is servicing {instrument.name}.")
        instrument.tune() # polymorphism

class Instrument:
    def __init__(self, name):
        self.name = name
    
    def tune(self): 
        raise NotImplementedError("Subclass must implement tune() function!") 
        # a backstop in case the specific Instrument object hasn't got a tune()

class Guitar(Instrument)
    def tune(self):
        print(f"Tuning the 6 strings of {self.name}...")
        sleep(0.5)
        print("Done!") 
       
```