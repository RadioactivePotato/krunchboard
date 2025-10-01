# krunchboard
A custom 80% ISO mechanical keyboard powered by a Raspberry Pi Pico with KMK

# Note

Prod V1 of the PCB has its I2C lines flipped for the 0.91" OLED Display and MCP23017

Firmware doesn't work yet

# About
I made this keyboard after I designed my [macropad](https://github.com/RadioactivePotato/krunchpad), and I thought this would be a fun project to do, I've also never owned a mechanical keyboard so maybe this is a good way to start?

# Images

![Schematic](assets/schematic.png)

| PCB | 3D View |
|-----|------------|
| ![PCB](assets/pcb.png) | ![3D-Front](assets/3dfront.png) |
| ![Case](assets/case.png) | ![3D-Back](assets/3dback.png) |

# Render

![Render1](assets/render1.png)

![Render2](assets/render2.png)

![Render3](assets/render3.png)

# BOM
| Qty | Item                               | Notes                                     | Cost (USD) | URL                                                                                                         |
|-----|------------------------------------|-------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------|
| 1   | Raspberry Pi Pico                  | USB-C Clone                               | 2.30       | [AliExpress](https://www.aliexpress.com/item/1005006067365069.html)                                         |
| 1   | EC11 Rotary Encoder                |                                           | 2.54       | [AliExpress](https://www.aliexpress.com/item/1005008413622715.html)                                         |
| 1   | Rotary Encoder Knob                |                                           | 0.98       | [AliExpress](https://www.aliexpress.com/item/1005007951780072.html)                                         |
| 92  | Kailh MX Hotswap Socket            | Hotswapping for switches                  | 7.88       | [AliExpress](https://www.aliexpress.com/item/1005007476614771.html)                                         |
| 1   | 0.91" OLED Display                 |                                           | 2.06       | [AliExpress](https://www.aliexpress.com/item/1005007672413060.html)                                         |
| 1   | 0.96" OLED Display                 |                                           | 2.18       | [AliExpress](https://www.aliexpress.com/item/1005006985022252.html)                                         |
| 1   | MX Stabilisers Set                 | For big keycaps                           | 4.37       | [AliExpress](https://www.aliexpress.com/item/1005009345248282.html)                                         |
| 93  | 1N4148W Diode (SOD-123)            | Already have                              | 0.50       | [LCSC](https://www.lcsc.com/product-detail/C42441811.html)                                                  |
| 1   | MCP23017 GPIO Expander (SOIC-28)   | Already have                              | 1.94       | [LCSC](https://www.lcsc.com/product-detail/C629440.html)                                                    |
| 2   | 4 Slot 2.54mm Socket               | Already have                              | 0.43       | [LCSC](https://www.lcsc.com/product-detail/C7509546.html)                                                  |
| 6   | SK6812MINI-E / SK6812E Neopixel    | Already have                              | 0.74       | [LCSC](https://www.lcsc.com/product-detail/C5149201.html)                                                   |
|     |                                    |                                           |            |                                                                                                             |
| 1   | Keycaps Set                        |                                           | 13.94      | [AliExpress](https://www.aliexpress.com/item/1005009177442825.html)                                         |
| 87  | Linear Key Switch                  | Main keyboard switches                    | 9.31       | [AliExpress](https://www.aliexpress.com/item/1005002378701948.html)                                         |
| 5   | Tactile MX-Style Switch            | Shortcut keys switches                    | 2.00       | [AliExpress](https://www.aliexpress.com/item/1005009249474760.html)                                         |
| 6   | Sticky rubber feet                 | Antislip for keyboard                     | 1.26       | [AliExpress](https://www.aliexpress.com/item/1005006832476105.html)                                         |
|     |                                    |                                           |            |                                                                                                             |
| 12  | M3x5mmx4mm Heatset Inserts (W\*H)  | For mounting                              | 2.13       | [AliExpress](https://www.aliexpress.com/item/1005007640664497.html)                                         |
| 12  | M3x5mm Screws                      | For case assembly                         | 2.44       | [AliExpress](https://www.aliexpress.com/item/1005006621501802.html)                                         |
|     |                                    |                                           |            |                                                                                                             |
| 1   | Solder Paste                       | Reflow soldering for SMD                  | 5.11       | [AliExpress](https://www.aliexpress.com/item/1005009377104599.htm)                                          |
| 1   | Solder Wire                        | 50g                                       | 3.32       | [AliExpress](https://www.aliexpress.com/item/1005008053204920.html)                                         |
|     |                                    |                                           |            |                                                                                                             |
| 1   | 3D Printed Case                    | print-legion postage (via royal mail)     | 7.00       | print-legion                                                                                                |
| 1   | PCB                                | Shipping $12.89                           | 41.79      | JLCPCB                                                                                                      |
|     |                                    |                                           |            |                                                                                                             |
|     |                                    | **Total AliExpress (GBP)**                | **61.82**  |                                                                                                             |
|     |                                    | **PCB and Case (GBP)**                    | **48.79**  |                                                                                                             |
|     |                                    | Total (USD)**                             | **103.61** |                                                                                                             |


![A badge of a Cerberus and a raccoon laughing together, with the text "HIGHWAY" and "HACK CLUB" beside them.](https://hc-cdn.hel1.your-objectstorage.com/s/v3/0bbcca68ffa3845300bb76940f8ad91fd53d2d68_06-30-2025-1618.png)
