# Python Projects

These projects were created in Python3 from the course materials for the PCEP qualification.

The projects explore various fundamental concepts in Python3.

## prison_break.py

You are a prison guard in a prison. The prison is represented by a list:

    []

The cells are represented by the list's elements, and consist of 1s and 0s:

    [1, 1, 0, 0, 0, 1, 0]

A 1 represents an unlocked cell, and a 0 represents a locked cell.

One night, you decide to stage a prison break!  
Starting from the left, and moving to the right, you open as many cells as you can.  
Unfortunately, there's a catch. The mechanism that controls the doors is malfunctioning.  
Every time you open the door to an unlocked cell, all of the cell doors invert.  
All of the locked cells unlock, and all of the unlocked cells lock.

    [1, 1, 0, 0, 0, 1, 0] --becomes--> [0, 0, 1, 1, 1, 0, 1]

You only have time to do this once, and there's no going back - the other guards are after you!

How many prisoners can you free?
