# WAPerceptionCodingChallenge

### Libraries used: 
- OpenCV
- NumPy

### My general approach: 
1. Read the image
2. Find all pixels where the image is red
3. Find midpoints of clusters of pixels where the image detected red
4. Connect those midpoints together with a line

### A more detailed explanation: 
- First, I thought about how I'd need to read the image file. This would require downloading ``red.png`` and analyzing its pixel data. 
I had to convert from a BRG to HSV image which I did using the ``cv2.cvtColor()`` method.

- I knew that the cones are red, so next I used OpenCV to find areas where there was sufficient red present. This means that there was a range of 
values for HSV so that I'm not just looking for one very specific color value, but that I also include for natural variation in lighting and whatnot.

- Next, I set up some debugging tools. This included showing a preview of ``answer.png`` in a new window titled 'Debug'; I used the ``cv.rectangle()``
method to have a red rectangle show around the areas where red was detected. I also tweaked around with some of its inputs such that there was a text
label of the coordinates of the red rectangle's midpoints. 

- I used this to figure out how to split the image into three parts. What I mean is that OpenCV was detecting red in the image a little too well. I looked
and saw that the exit sign and the door near the top right of the picture were also being detected as having red. What I did to combat this is ignore any 
red pixel detection from the upper part of the image, which corresponded to a y-value of less than 600. 

- Next I also used the debugging tools to figure out which x-values corresponded to which line of cones. What I mean is that the cones are obviously setup
in two lines, a left line on the left side of the image and a right line on the right side of the image. I created two arrays titled ``pointsLeft`` and 
``pointsRight`` which stored the coordinates of the detected red areas depending on whether they were not a part of the upper part of the image (as discussed
 in the previous point) and did or did not have an x-value of greater than 1000. An x-value of 1000 or greater meant that the cone was part of the right side
 of the image; anything less was considered to be part of the left side of the image.
 
 - Then, I set up starting and ending points for the two lines, left and right. These starting and ending points were the 0th index element and the -1 index 
 element of their respective arrays. This meant that if part of the ``pointsLeft`` array, the starting point was ``pointsLeft[0]`` and the ending point 
 was ``pointsLeft[-1]``; the same was the case for ``pointsRight``.
 
 - Lastly, I used the ``cv2.line()`` method to trace 5 pixel wide lines from the starting and ending points of the respective left and right cone lines. I tried 
 to figure out how to use a best fit line, but I ran into trouble and wasn't able to find enough help online. I probably didn't look well enough, but then I 
 just used a roundabout solution to try to achieve something close to what was expected. I think the result is fine; it's not the best but neither the worst.
 
 ### My ``answer.png`` file: 
 
 ![answer](https://user-images.githubusercontent.com/43867336/223019042-58dbe704-bff2-4657-8db6-2727eabab7d6.png)
