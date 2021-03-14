# ThingPulse Icon64 Bluetooth Speaker

ESP32 based Bluetooth loudspeaker with 8 band spectrum analyzer. This is the stock firmware for the [ThingPulse Icon64](https://thingpulse.com/product/icon64/) devices.

## Minor changes by me (msimon4u@gmx.de)

Hardware: Connect GAIN to GND, otherwise loudness is changing during playing music

Software: Minor changes to platformio.ini [new board](https://github.com/michaelsimon101/esp32-icon64-a2dp/blob/cc46dcab6afb7aa1afbba30b0831fc3a201c8d4e/platformio.ini#L33) and to src/main.cpp for Az-Delivery 8x8 LED Matrix [getLedIndex](https://github.com/michaelsimon101/esp32-icon64-a2dp/blob/cc46dcab6afb7aa1afbba30b0831fc3a201c8d4e/src/main.cpp#L94)

[![ThingPulse Icon64](https://thingpulse.com/wp-content/uploads/2020/11/Whitebox_Heart.jpg)](https://thingpulse.com/product/icon64/)

[![YouTube demo](http://img.youtube.com/vi/1UpbtE98OBA/0.jpg)](http://www.youtube.com/watch?v=1UpbtE98OBA "Icon64 Bluetooth Speaker")
[► Video](http://www.youtube.com/watch?v=1UpbtE98OBA "Icon64 Bluetooth Speaker")
