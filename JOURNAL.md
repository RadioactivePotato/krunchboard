---
title: "krunchboard"
author: "slack: krunch"
description: "Tenkeyless ISO105  mechanical keyboard"
created_at: "2025-06-26"
---

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
