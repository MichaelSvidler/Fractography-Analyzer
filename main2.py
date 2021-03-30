from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import messagebox
from PIL import Image
from pylab import *
import numpy as np
import cv2


mask_path = ''
image_path = ''
selected_path = ''
selected_ratio = 0
ratio = 0

num_of_masked = 0
num_of_cropped = 0
pt = []


# load the mask image
def load_mask():
    global mask_path
    mask_path = askopenfilename()

    return mask_path


# load the real image
def load_image():
    global image_path
    image_path = askopenfilename()


# load image to  manually crop
def load_selected():
    global selected_path
    selected_path = askopenfilename()


# apply the mask on the real image
def apply_mask():
    global num_of_masked

    if image_path == '':
        messagebox.showinfo('Error', 'You have not loaded an image yet')

        return image_path

    elif mask_path == '':
        messagebox.showinfo('Error', 'You have not loaded a mask image yet')

        return mask_path

    else:
        img = cv2.imread(image_path)
        mask = cv2.imread(mask_path)

        # apply the mask
        masked_image = cv2.bitwise_and(img, mask)

        # save the result
        num_of_masked = num_of_masked + 1
        res = 'images/masked_image_' + str(num_of_masked) + '.png'
        cv2.imwrite(res, masked_image)
        print("this main")
        return res


# edge detection using CLAHE (to enhance contrast) and Canny (to detect edges)
def edge_detect():
    # Read the image.
    img = cv2.imread(image_path)

    # Contrast enhancement - CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8, 8))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    lab = cv2.merge((l2, a, b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR

    # Edge detection using Canny
    edges = cv2.Canny(img2, 200, 300)
    cv2.imwrite('edges.jpg', edges)

    plt.subplot(121), plt.imshow(img2, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()


# calculate the average slope of all lines
def avg_slope(lines):
    count = 0
    mt = 0

    for line in lines:
        x1, y1, x2, y2 = line[0]
        count = count + 1

        m = (y2 - y1) / (x2 - x1)
        mt = mt + m

    m_avg = mt / count  # average slope of all lines

    return m_avg


# line detection using Hough Transform
def line_detect():
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=250)

    m_avg = avg_slope(lines)

    xt1, yt1, xt2, yt2 = 0, 0, 0, 0
    x1_prev, x2_prev, y1_prev, y2_prev = 0, 0, 0, 0
    flag2 = 0
    count = 0

    for line in lines:
        if flag2 == 1:
            x1_prev, x2_prev, y1_prev, y2_prev = x1, x2, y1, y2

        x1, y1, x2, y2 = line[0]
        m = (y2 - y1) / (x2 - x1)  # the line's slope
        m_diff = abs(m - m_avg)  # absolute value of the difference between the line's slope and the average one

        #dist1 = math.hypot(x1_prev - x1, y1_prev - y1)
        #dist2 = math.hypot(x2_prev - x2, y2_prev - y2)
        #dist_avg = (dist1 + dist2) / 2

        #x1_new = int((x1 + x1_prev) / 2)
        #x2_new = int((x2 + x2_prev) / 2)
        #y1_new = int((y1 + y1_prev) / 2)
        #y2_new = int((y2 + y2_prev) / 2)

        #m_new = (y2_new - y1_new) / (x2_new - x1_new)
        #m_new_diff = abs(m_new - m_avg)

        #xt1 = xt1 + x1
        #yt1 = yt1 + y1
        #xt2 = xt2 + x2
        #yt2 = yt2 + y2

        # filtering the lines with largely different slope
        if m_diff < 1.1:
            xt1 = xt1 + x1
            yt1 = yt1 + y1
            xt2 = xt2 + x2
            yt2 = yt2 + y2
            if count == 0:
                x1_first, y1_first, x2_first, y2_first = x1, y1, x2, y2

            flag2 = 1
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), thickness=2)
            #if dist_avg > 50 and m_new_diff < 1.5:
            #    print(m_avg)
            #    cv2.line(img, (x1_new, y1_new), (x2_new, y2_new), (0, 0, 128), thickness=2)
            #    count = count + 1
            count = count + 1

            x1_last, y1_last, x2_last, y2_last = x1, y1, x2, y2
        else:
            flag2 = 0

    dist1 = math.hypot(x1_last - x1_first, y1_last - y1_first)
    dist2 = math.hypot(x2_last - x2_first, y2_last - y2_first)
    dist_avg = (dist1 + dist2) / 2
    real_dist = dist_avg * ratio
    real_dist = real_dist / count
    print('density: ', 1 / real_dist, 'count: ', count)

    xt1 = int(xt1 / count)
    yt1 = int(yt1 / count)
    xt2 = int(xt2 / count)
    yt2 = int(yt2 / count)

    deltaY = yt2 - yt1
    deltaX = xt2 - xt1
    angleInDegrees = arctan(deltaY / deltaX) * 180 / 3.141592654

    m1 = (yt2 - yt1) / (xt2 - xt1)
    m2 = 0
    tg_ang = abs((m2 - m1) / (1 + (m1 * m2)))
    print('points: ', xt1, xt2, yt1, yt2)
    print('angle: ', angleInDegrees)

    # draw the average of all lines - the direction of the fracture
    # plus or minus 50 to make the line longer
    cv2.line(img, (yt1 - 50, xt2 + 50), (yt2 + 50, xt1 - 50), (0, 128, 0), thickness=3)

    cv2.imshow("linesEdges", edges)
    cv2.imshow("linesDetected", img)
    cv2.imwrite('images/lines.png', img)


# select number of points on the image in order to crop it
def select():
    global selected_path
    selected_path = askopenfilename()

    if selected_path == '':
        messagebox.showinfo('Error', 'You have not loaded an image yet')

        return selected_path
    else:
        global pt
        num_of_points = 4

        im = Image.open(selected_path)
        im = im.convert('RGB')
        img = array(im)
        imshow(img)
        # Select 4 points
        pt = ginput(num_of_points)

        print('You selected : ', pt)

        if num_of_points == 4:
            matplotlib.pyplot.close(fig=1)
            return crop()

        show()


def select_ratio():
    global selected_ratio
    global ratio
    selected_path = askopenfilename()

    if selected_path == '':
        messagebox.showinfo('Error', 'You have not loaded an image yet')

        return selected_path
    else:
        global pt
        num_of_points = 2

        im = Image.open(selected_path)
        im = im.convert('RGB')
        img = array(im)
        imshow(img)
        # Select 2 points
        pt = ginput(num_of_points)

        print('You selected : ', pt)

        if num_of_points == 2:
            selected_ratio = pt
            x1 = pt[0][0]
            y1 = pt[0][1]
            x2 = pt[1][0]
            y2 = pt[1][1]

            ratio = math.hypot(x2 - x1, y2 - y1)
            ratio = 10 / ratio
            print(ratio)
            matplotlib.pyplot.close(fig=1)



# crop the image by the selected points
def crop():
    global num_of_cropped

    x1 = int(pt[0][0])
    y1 = int(pt[0][1])
    x2 = int(pt[1][0])
    y2 = int(pt[1][1])
    x3 = int(pt[2][0])
    y3 = int(pt[2][1])
    x4 = int(pt[3][0])
    y4 = int(pt[3][1])

    # original image
    image = cv2.imread(selected_path)
    contours = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])

    # create the mask according to the selected points
    mask = np.zeros(image.shape, dtype=np.uint8)
    cv2.fillPoly(mask, pts=[contours], color=(255, 255, 255))

    # apply the mask
    masked_image = cv2.bitwise_and(image, mask)

    # save the result
    num_of_cropped = num_of_cropped + 1
    res = 'images/cropped_image' + str(num_of_cropped) + '.png'
    cv2.imwrite(res, masked_image)

    return res
