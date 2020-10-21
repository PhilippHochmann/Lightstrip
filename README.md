# Lightstrip

## MCU
MCU just takes serial data to display on the LED strip.
Compile and flash with ```make flash```.
Don't forget to adjust USB device in Makefile and to ```chmod 666``` it if necessary.

## PC
The PC computes cool looking effects and sends them via USB to the MCU.
Compile and run with ```make run```.
Don't forget to adjust USB device in PC Makefile (usually the same as in MCU Makefile) because running the application
means opening a serial connection over this port.

## Sources

https://www.embeddedrelated.com/showarticle/528.php
https://blog.mbedded.ninja/programming/operating-systems/linux/linux-serial-ports-using-c-cpp/#basic-setup-in-c