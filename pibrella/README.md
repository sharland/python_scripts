#Pibrella and Python


This is my own documentation on using the pibrella and the Raspberry pi.  Original instructions from Gadgetoid [here](https://github.com/pimoroni/pibrella/blob/master/README.md) summarised a little bit.

##Installation

##Running Pibrella

Pibrella requires access to your GPIO which requires sudo.  Therefore run anything as `sudo python example.py`

You will need to `import pibrella` at the beginning of your python script

##Lights

red
amber
green

1. Single light off and on
* `pibrella.light.red.on()`
* `pibrella.light.red.off()`
2. All lights off and on
* `pibrella.light.on()`
* `pibrella.light.off()`
3. Blinking lights (remove red for all lights to blink)
    ON_TIME = 0.5
    OFF_TIME = 0.5
    
    pibrella.light.red.blink(ON_TIME, OFF_TIME)
4. Fading lights (remove red for all lights to fade)
    FADE_IN_TIME = 0.5
    FADE_OUT_TIME = 0.5
    ON_TIME = 0.5
    OFF_TIME = 0.5
    
    pibrella.light.red.fade(FADE_IN_TIME,FADE_OUT_TIME,ON_TIME,OFF_TIME)
5. Fading lights
* `pibrella.light.red.fade(0, 100, 2) # From 0 to 100% in 2 seconds`

##Button

##Speaker
