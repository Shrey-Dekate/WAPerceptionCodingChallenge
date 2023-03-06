import cv2
import numpy as np

# cv2 "reads" the image
def getPicture(image):
    imageOutput = cv2.imread(image)
    return imageOutput

# the main part of the program, identifies, stores, and draws lines for where the cones are
def colorBounds(imageFrame):
    # converting from bgr to hsv
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # setting limits for what constitutes as a "red" color
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    
    kernal = np.ones((5, 5), "uint8")
      
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask = red_mask)
   
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)          

    # arrays used later to store the respective coordinates of the left-side and right-side cones
    pointsLeft = []
    pointsRight = []

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 200):
            x, y, w, h = cv2.boundingRect(contour)

            # if the "red detected" is too far "up" in the image, ignore it!
            # this has been put in place because a part of the door in the top right was being detected
            # and the exit sign, which are not cones

            if (y < 600):
                break
            
            # used for debugging, a red rectangle would show around each detected cone

            # imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            if (x > 1000):
                pointsRight.append((x,y))
            else: 
                pointsLeft.append((x,y))

            # used for debugging

            # cv2.putText(imageFrame, "Red Colour: ("+str(x)+", "+str(y)+")", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

    # debug statements used to verify adding respective points was working

    # print("pointsLeft: ", pointsLeft)
    # print("pointsRight", pointsRight)

    # setting up the starting and end point for the left-side cones
    start_point_left = pointsLeft[0]
    end_point_left = pointsLeft[-1]

    # setting up the starting and end points for the right-side cones
    start_point_right = pointsRight[0]
    end_point_right = pointsRight[-1]

    color = (0, 0, 255) # color is (blue, green, red)
    thickness = 5       # thickness in pixels!

    # draws both lines for the left-side cones and the right-side cones
    imageFrame = cv2.line(imageFrame, start_point_left, end_point_left, color, thickness)
    imageFrame = cv2.line(imageFrame, start_point_right, end_point_right, color, thickness)

    # frame resizing used to better debug code
    
    # imageFrame = cv2.resize(imageFrame, (700, 850))
    # cv2.imshow("Debug", imageFrame)
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()

    cv2.imwrite("answer.png", imageFrame)
    

if __name__ == "__main__":
    imageOrigin = getPicture("red.png")
    colorBounds(imageOrigin)