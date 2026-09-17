```{trouble}
I have re-flashed the HUT, but my Duckiebot still does not move or moves in a jerky manner. Additionally, the ToF sensor and front bumper are not detected on the `Components` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page robot/components`). I may also be having issues with the screen.
---
Disconnect the ToF sensor from the front bumper, then use the long I2C cable that originally connected the front bumper to the HUT to connect the ToF sensor directly to the same HUT port. Finally, reboot your Duckiebot. This procedure bypasses a known multiplexer issue on some front bumpers that can cause other issues with the HUT.
```
