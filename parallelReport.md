Report - Nestor Escobedo -  Lab 1 part 2

When doing this assignement Ifound had some trouble to figure out which part of the algorithm to parallelize, I was trying to figure which of the loops was better to use, but the professor said that whichever loop would work for this assignment so I just pciked one.

I also had some issues with the cpuInfo.sh file I could not get it to work because I was getting some of the permissions denied. I had to use chmod to enable those permissions  and get it to work.

This lab took me around 3 hours to complete because I had to revauluate my previous code.

There might be an issue with the timing in the program because it is not being  consistent, with what was mentioned in class.

Results:

- 1 threads: 0.4512
- 2 threads: 0.2364
- 4 threads: 0.0938
- 8 threads: 0.0941

The conclusion for this program is that the threads drastcally reduces its time when usign 2 threads versus 1, then the time decreases but not in a significant way, and finally int the 8 threads the time goes a little bit up from 4 threads probably because of overhead.