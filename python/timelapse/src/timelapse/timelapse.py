import picamera
import logging
from PIL import Image, ImageChops
from time import sleep

global prevImage

# Constants

PATH = 'tlphotos/'
FILENAME_DIFF_IMAGE = 'tmpDiffPicture.jpg'
FILENAME_TMP_IMAGE = 'tmpPicture.jpg'
THRESHOLD = 0.0001
SLEEP_DIFF_SEC = 3
SLEEP_TIMELAPSE_SEC = 0.1
NUMBER_OF_PICTURES = 20
TIME_LAPSE = 100000

# image1 grayscaled image
# image2 grayscaled image
# 
def getBrightDarkRatio(image1, image2, saveDiffImage = False):
    diffImage = ImageChops.difference(image1, image2)
    if saveDiffImage:
        diffImage.save(PATH + FILENAME_DIFF_IMAGE)
    histogram = diffImage.histogram()
    return calculateRatio(histogram, 256)

def calculateRatio(array, lengthOfBand):
    assert lengthOfBand % lengthOfBand == 0
    dark = 0
    bright = 0
    for i in range(lengthOfBand):
        if i < lengthOfBand/2:
            dark += array[i]
        else:     
            bright += array[i]
    ratio = float(bright) / float(dark + bright)        
    return ratio

def takeGrayscaledPicture(camera):
    imageFile1 = open(PATH + FILENAME_TMP_IMAGE, 'wb')
    camera.resolution = (640, 480)
    camera.color_effects = (128, 128)
    camera.capture(imageFile1)
    imageFile1.close()
    return Image.open(PATH + FILENAME_TMP_IMAGE)

def watch(camera):
    image = takeGrayscaledPicture(camera)
    brigthDarkRatio = getBrightDarkRatio(image, prevImage)
    logging.info('Difference: ' + str(brigthDarkRatio))
    if (brigthDarkRatio >  THRESHOLD):
        logging.info('start time-lapse: number of pictures ' + str(NUMBER_OF_PICTURES) + '  every ' + str(SLEEP_TIMELAPSE_SEC) + ' second(s)')
        takePictures(camera)
    else:
        logging.info('no difference, wait for ' + str(SLEEP_DIFF_SEC) + ' seconds')
        sleep(SLEEP_DIFF_SEC)
    global prevImage 
    prevImage = image    
    
def takePictures(camera):
    camera.resolution = (1920, 1080)
    camera.color_effects = None
    for i, filename in enumerate(camera.capture_continuous(PATH + '{timestamp:%y%m%d%H%M%S%f}_time-lapse_{counter:03d}.jpg')):
        print(filename)
        sleep(SLEEP_TIMELAPSE_SEC)
        if i == NUMBER_OF_PICTURES-1:
            break

def initCamera(camera):
    global prevImage 
    prevImage = takeGrayscaledPicture(camera)

if __name__ == "__main__":
    logging.basicConfig(filename='timelapse.log',level=logging.INFO)
    logging.info('start camera')
    with picamera.PiCamera() as camera:
        camera.start_preview()
        sleep(2)
        camera.stop_preview()        
        initCamera(camera)
        logging.info('start time-lapse')
        for i in range(TIME_LAPSE):
            watch(camera)
        logging.info('end time-lapse')
   


