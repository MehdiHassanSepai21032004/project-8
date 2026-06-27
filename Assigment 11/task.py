import cv2
import numpy as np


def image():
    # for read image
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg", 1)
    print("Dimension of image:", img.shape)

    height = 800
    width = 900
    dim = (height, width)
    resize = cv2.resize(img, dim)

    cv2.imshow("image", img)
    cv2.imwrite("bird.jpg", img)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def matrix():
    # load image
    image = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")
    # Image shape & size
    height = 800
    width = 900
    dim = (height, width) # Height & width
    resized = cv2.resize(image, dim)

    kernel = np.ones((5,5), dtype= 'uint8') # kernel edit
    # Erosion on this image
    erosion = cv2.erode(resized, kernel,iterations = 1)
    # Dilation on this image
    dilation = cv2.dilate(resized, kernel, iterations = 1)
    # Opening on this image
    opening = cv2.morphologyEx(resized,cv2.MORPH_OPEN, kernel)
    # Closing on this image
    closing = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)
    # Tophat on this image
    tophat = cv2.morphologyEx(resized,cv2.MORPH_TOPHAT, kernel)
    # Blackhat on this image
    blackhat = cv2.morphologyEx(resized, cv2.MORPH_BLACKHAT,kernel)
    # Gradient on this image
    gradient = cv2.morphologyEx(resized,cv2.MORPH_GRADIENT,kernel)

    cv2.imshow("Original" , resized)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Dilation", dilation)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)
    cv2.imshow("Tophat", tophat)
    cv2.imshow("Blackhat", blackhat)
    cv2.imshow("Gradient", gradient)

    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def flip():
    # Load the image
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not load image.")
        return

    # Resize image
    width = 400
    height = 400
    dim = (width, height)  # (width, height)

    resized = cv2.resize(img, dim)

    # Show original resized image
    cv2.imshow("Original", resized)

    # Flip horizontally
    flip_1 = cv2.flip(resized, 1)
    cv2.imshow("Horizontal", flip_1)

    # Flip vertically
    flip_2 = cv2.flip(resized, 0)
    cv2.imshow("Vertical", flip_2)

    # Flip horizontally and vertically
    flip_3 = cv2.flip(resized, -1)
    cv2.imshow("Horizontal & Vertical", flip_3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")
    print("Dimension of original image:", img.shape)
    scale = 50
    width = int(img.shape[1]*scale/100)
    height = int(img.shape[0]*scale/100)
    dim = (width, height)
    resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
    print("Dimension of the image:" , resized)
    cv2.imshow("Original", img)
    cv2.imshow("resized", resized)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def shape_text():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg", cv2.IMREAD_COLOR)
    cv2.line(img,(0,0),(150,150),(250,0,0), 2)
    cv2.rectangle(img,(200,150,), (250,300),(0,255,0),3)
    cv2.circle(img,(300,75), 70,(255,0,255), 3)
    pts_polygon = np.array([[100,50],[100,300],[500,50],[500,300]], np.int32)
    cv2.polylines(img,[pts_polygon], True, (0,255,255),3)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, "Hello", (10,500),font, 3,(200,255,255), 8, cv2.LINE_AA)

    cv2.imshow("Image", img)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def shifting():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")
    column = img.shape[1]
    row = img.shape[0]
    s = np.float32([(1,0,150), (0,1,70)])
    shifted = cv2.warpAffine(img, s, (column, row))
    cv2.imshow("Original", img)
    cv2.imshow("shifted", shifted)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()
    
def rotation():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")
    column = img.shape[1]
    row = img.shape[0]
    center = (column /2, row/2)
    angle = 180
    r = cv2.getRotationMatrix2D(center,angle,1)
    rotate = cv2.warpAffine(img,r,(column,row))
    cv2.imshow("Rotate", rotate)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def thresolding():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg",0)
    thresold_value = 100
    _,binary_thresold = cv2.threshold(img,thresold_value,255,cv2.THRESH_BINARY)
    cv2.imshow("Original", img)
    cv2.imshow("Binary_Thresold", binary_thresold)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def gaussian_blur():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg",1)
    resize = cv2.resize(img, (640,640))
    ksize = (7,7)
    sigmax = 0
    sigmay = 0
    blur = cv2.GaussianBlur(resize,ksize,sigmax)
    cv2.imshow("input", resize)
    cv2.imshow("Output", blur)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def median_blur():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")
    resize = cv2.resize(img,(650,650))
    kernel = 3
    blur = cv2.medianBlur(resize,kernel)
    cv2.imshow("Input", resize)
    cv2.imshow("Output", blur)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()

def bilateral_filter():
    # Read the image
    image = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg")

    # Check if the image loaded successfully
    if image is None:
        print("Error: Could not load the image.")
        return
    
    # Resize the image
    resized = cv2.resize(image, (520, 520))
    # Bilateral filter parameters
    d = 7
    sigmaColor = 100
    sigmaSpace = 100
    # Apply bilateral filter
    b = cv2.bilateralFilter(resized, d, sigmaColor, sigmaSpace)
    # Display images
    cv2.imshow("Original", resized)
    cv2.imshow("Output", b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def edge_detection():
    img = cv2.imread("/Users/mehdihassansepai/Downloads/bird.jpg",0)
    resize = cv2.resize(img,(520,520))
    min_thresh = 100
    max_thresh = 200
    edge = cv2.Canny(resize,min_thresh, max_thresh)
    cv2.imshow("Original", resize)
    cv2.imshow("Output", edge)
    cv2.waitKey(0) == ord("Q")
    cv2.destroyAllWindows()
    
def video(): 
    video = cv2.VideoCapture("/Volumes/SUNDISK/Pixel Phone Documents/Quick Share/vid.mp4")
    while video.isOpened():
        _,frame = video.read()
        frame = cv2.resize(frame,(800,720))
        cv2.imshow("Output", frame)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()

def write_video():
    video = cv2.VideoCapture("/Volumes/SUNDISK/Pixel Phone Documents/Quick Share/vid.mp4")
    fourcc =cv2.VideoWriter.fourcc(*'mpv4')
    output = cv2.VideoWriter('output.mp4', fourcc,25.0,(1920,1080))
    while video.isOpened():
        ret,frame = video.read()
        if ret:
            output.write(frame)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(10) == ord("z"):
                break
        else:
            break
    cv2.destroyAllWindows()


def live_video():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        _,frame = cap.read()
        cv2.imshow("Live", frame)
        if cv2.waitKey(10) == ord('z'):
            break
        cv2.destroyAllWindows()

image()
matrix()
flip()
resize()
shape_text()
shifting()
rotation()
thresolding()
gaussian_blur()
median_blur()
bilateral_filter()
edge_detection()
video()
write_video()
live_video()