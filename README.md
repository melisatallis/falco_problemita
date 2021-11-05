# Reorder a sequence of images that were placed out of order

In this work, we attempt to recover the unknown order of an image sequence captured by a single, stationary camera. Assuming we know the first frame in our sequence, there can be a total of (n-1)! possibilities for the sequence order. Given the complexity of the task, we choose to analyze non-looping, short sequences of dynamic scenes (i.e - person kicking a ball). This means that the differences between images accumulate with time. La diferencia por pixel entre cuadrosWe find that We then see how well our algorithm performs on a few image sequences that have been randomly shuffled. 

This repository contains an iPython notebook that walks you through the steps taken in order to reorder the shuffled image sequence. 

``data`` contains source GIF files used to test the algorithm. 
``figures`` contains source GIF files used to test the algorithm. 

[working repository]: