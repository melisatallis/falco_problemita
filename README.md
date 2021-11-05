# Reorder a sequence of images that were placed out of order

In this work, we attempt to recover the unknown order of an image sequence captured by a single, stationary camera. Assuming we know the first frame in our sequence, there can be a total of (n-1)! possibilities for the sequence order. Given the complexity of the task, we choose to analyze continous, short, non-looping sequences of dynamic scenes (i.e - person kicking a ball). Meaning that we look for differences that accumulate with time. As a start, we order images by the total number of zeros present after computing the difference between correspondin pixels of two frames. MOre zeros implies less time has passed. We apply our algorithm on a few few image sequences that have been randomly shuffled and score its performance. 

This repository contains an iPython notebook that walks you through the steps taken in order to reorder the shuffled image sequence. 

``data`` contains source GIF files used to test the algorithm. 
``figures`` contains the figures displayed in teh notebook. 
