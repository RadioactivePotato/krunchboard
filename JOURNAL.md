---
title: "krunchboard"
author: "slack: krunch"
description: "A 85% ISO mechanical keyboard powered by Raspberry Pi Pico"
created_at: "2025-06-26"
---

# Total time spent: 26 hours

# June 26th - Made the schematic (3 hours)

<details>
<summary>Click to expand</summary>

Made the basic schematic with the ISO105 layout, but without the number pad.

Had to use a gpio expander because I was running low on pins

I used [keyboard-layout-editor.com](https://keyboard-layout-editor.com) and [kbfirmware.com](https://kbfirmware.com) to help.

![image](https://github.com/user-attachments/assets/db71ca8c-b90c-4bf3-b1fc-a7ff3e9036f3)

![image](https://github.com/user-attachments/assets/c9521a2d-a574-43d5-9240-c7bb2673539b)

**Time spent this session: 3 hours**

</details>

# June 27th - Placed the components (4 hours)

<details>
<summary>Click to expand</summary>

Followed this diagram

![image](https://github.com/user-attachments/assets/4e4d62dd-5f5d-4fda-b327-d8a1f31ce71e)

Spent quite a while trying to get the key switches to not overlap, but [this video](https://www.youtube.com/watch?v=8WXpGTIbxlQ&t=864s) helped a ton!

I switched the diodes and gpio expander from THT to SMT, it might be harder to solder but it's going ot look much better!

## Progress

![image](https://github.com/user-attachments/assets/78620c9c-ef76-48fd-94ef-a406fb5a7deb)

![image](https://github.com/user-attachments/assets/ec2bc2c4-b2ae-4306-aa40-87844536fc19)

## Finished the PCB layout

![image](https://github.com/user-attachments/assets/7441c98a-7816-467f-8b47-980b4c68fcb5)

![image](https://github.com/user-attachments/assets/b6367f41-5c08-495b-9791-179816e14cf7)

![image](https://github.com/user-attachments/assets/6ad96a0e-b215-4644-9d2c-473ede2da245)

**Time spent this session: 4 hours**

</details>

# June 28 - Redid the entire schematic (3.5 hours)

<details>
<summary>Click to expand</summary>

I decided to make the function key row closer to the number row, i also switched the oled from 0.96" to 0.91".

I added 5 programmable macro keys on the right and moved the volume knob to the top right.

Unfortunately I had to redo the schematic and pcb because when I changed the size of the keycaps, the column number also changed as well, which basically moved all of the keys to a new column

![image](https://github.com/user-attachments/assets/91ebcadd-7659-4b8b-8e29-64e5aa94f7e9)


![image](https://github.com/user-attachments/assets/30d7db14-7c61-4b99-b81d-be9808838b1b)

![image](https://github.com/user-attachments/assets/fe0216b5-0d94-4171-b173-546aba6a463b)

![image](https://github.com/user-attachments/assets/ff9d8d8a-ada1-4bc3-8165-e34c24130263)

**Time spent this session: 3.5 hours**

</details>


# June 30th - Placed the diodes ...again (2 hours)

<details>
<summary>Click to expand</summary>

I rotated all the symbols for key switches in the schematic by 180 degrees so that the wiring would be much cleaner, I originally tried to make a script that does that in one go, but I gaved up and decided to just rotate them all manually <img src="https://cdn.discordapp.com/emojis/1357156702943973376.webp?size=80" alt="" width="25" height="25">

I also placed all the diodes on the PCB, and whilst wiring up the columns, I realised that the row traces will block the connection

![image](https://github.com/user-attachments/assets/d28fbd1f-13dd-410f-90f1-77ff33e12cb1)

And since the hotswap sockets and diodes are both surface mounted, I'd have to create a via at all the column connections

![image](https://github.com/user-attachments/assets/5cf23016-af97-40ce-85c8-3b2a16c5ed5f)

Pretty sure I can just use the footprint that have the holes plated, that way I can just wire the column to the THT pad, I'll figure that out next time.

![image](https://github.com/user-attachments/assets/8aa9d298-7d9e-43e5-a7dd-9cd6c26c0b48)



**Time spent this session: 2 hours**

</details>

# July 8-9th - Started wiring the rows and columns (1.5 hours)

<details>
<summary>Click to expand</summary>

Like I mentioned in the last journal entry, i ran in to a "issue" where I would need to create multiple vias in order to properly wire the columns which I thought doesn't look as good, so I found a hotswap footprint with the hole being plated, this way, it can serve as a via (through hole) itself, and I won't have to place down multiple vias

| Before | After |
|--------|-------|
| ![image](https://github.com/user-attachments/assets/5cf23016-af97-40ce-85c8-3b2a16c5ed5f) | ![image](https://github.com/user-attachments/assets/1b03a554-eae5-4597-8c6f-dc0109909cd7) |

## NO VIAS!

Since I am now using a different footprint, I had to reassign the 3D models to the switches which took quite a while

Once I finished with that, I began wiring up the rows and columns!

![image](https://github.com/user-attachments/assets/87d88d12-1aef-48c4-81a0-a367e217164a)

It's now 00:15am <img src="https://cdn.discordapp.com/emojis/1357156702943973376.webp?size=80" alt="" width="25" height="25"> lol, I'll continue wiring up the rows tomorrow and will replace the neopixel footprint with a reverse mounted one.

**Time spent this session: 1.5 hours**

</details>

# July 9th - "Finished" PCB and Case (4 hours)

<details>
<summary>Click to expand</summary>

Today I finished wiring up the rows and columns of the PCB (I haven't connected it to the Pico yet since I still haven't decided the final location of the Pico).

I also added 6 M3 mounting holes for it to attach to the case and replaced the SK6812-Mini-E footprint with a reverse mountable one.

![image](https://github.com/user-attachments/assets/7be5c1fb-7d5c-467e-9f5c-fa689d81ff5d)

![image](https://github.com/user-attachments/assets/82c047aa-0207-4da6-a241-c66571dfffa6)

| Front | Back |
|-------|------|
| ![image](https://github.com/user-attachments/assets/8b727315-e696-4003-9f75-a62e2c3a1309) | ![image](https://github.com/user-attachments/assets/a6c96cf6-f1c3-4556-9b82-c1fdf4401b61) |

## Case Design

I designed it in OnShape, I started by placing the PCB layout (from 3D viewer) on the sketch, and then drew the slots for the components in the back of the PCB to sit in, I also added a few "beams" to support the middle of the PCB.

| - | - |
|---|---|
| ![image](https://github.com/user-attachments/assets/451418c7-7051-44d7-9edd-448f1bf769a9) | ![image](https://github.com/user-attachments/assets/2bc58864-22bf-49fd-b4eb-1104e176bf65) |

![image](https://github.com/user-attachments/assets/87276561-d8a4-45c6-95f7-bcd1cae5f7d2)

**Time spent this session: 4 hours**

</details>

# July 10th - Plate, BOM, and Files (4 hours)

<details>
<summary>Click to expand</summary>

Today I writtened the BOM in the README file, I also imported all the files necessary to the GitHub repo.

I used [keyboard-layout-editor.com](https://keyboard-layout-editor.com) and [kbplate.ai03.com](https://kbplate.ai03.com) to generate the DXF image, then I imported it to KiCad's `Edge.Cuts` layer. Since I have an OLED display and a rotary encoder, I had to manually draw the cutouts for it.

<img width="1010" height="370" alt="image" src="https://github.com/user-attachments/assets/1ff0dcf4-f46f-49e2-8a9a-15eb7fe3322f" />

I was originally going to use FR4 for the plate, but I soon realised that would be too expensive (about $60 incl. shipping), so I resorted to 3D printing. I exported the PCB as stl and imported it to Bambu studio, where I cut the model in half and it was able to fit on the print bed. I also did this for the case since it was also too big.

I will finish up the final bits of wiring on the main PCB and begin the firmware work (KMK). I should be able to submit this project over the weekend (July 12-13).

<img width="676" height="471" alt="image" src="https://github.com/user-attachments/assets/43f2cda3-331a-4a1d-8dcf-cd7f7f6ccabf" />
<img width="293" height="106" alt="image" src="https://github.com/user-attachments/assets/30ae0016-fc78-49e9-b732-ced44f662fb2" />

**Time spent this session: 4 hours**

</details>

# July 11 - Art and Firmware (4 hours)

<details>
<summary>Click to expand</summary>

Today I created the firmware, a large portion of the code is based on the ANAVI macropad 12's firmware, I followed my schematic and [the keycode list](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md) to code the keymaps.

I also finished up all the wiring on the pcb, It took quite a while and I had to move some of the traces which was originally going to the Pico, but now it's moved to the MCP23017.

Also used maybe too many vias lol

<img width="703" height="466" alt="image" src="https://github.com/user-attachments/assets/96af57ac-7f83-45fc-a0a9-5f8b26a18497" />
<img width="719" height="448" alt="image" src="https://github.com/user-attachments/assets/5d13f8d9-41d4-41dd-a128-fa05bf6c8b18" />
<img width="308" height="479" alt="image" src="https://github.com/user-attachments/assets/96df655d-6297-40e6-892d-875c64262945" />

To fill in the blank space in the back of the PCB, I converted the Highway artwork to KiCad silkscreen.

<img width="947" height="476" alt="image" src="https://github.com/user-attachments/assets/99359063-43f3-4336-acf5-c3b8758ad178" />

And then I added some silkscreen art to the front as well, and then added a 0.96" OLED display.

<img width="1100" height="379" alt="image" src="https://github.com/user-attachments/assets/83e25fe5-1e85-4b1f-8491-08f185fd612a" />

And that's the whole project done!

</details>
