import picamera
from time import sleep
from time import strftime


def takePictures(camera):
    camera.resolution = (2592, 1944)
    camera.color_effects = None
    for i, filename in enumerate(camera.capture_continuous('time-lapse{counter:02d}.jpg')):
        print(filename)
        sleep(0.5)
        if i == 60:
            break

def takeGrayscaledPicture(camera):
    imageFile1 = open(strftime("%y%m%d%H%M%S") + 'a_test.jpg', 'wb')
    camera.resolution = (640, 480)
    camera.color_effects = (128, 128)
    camera.capture(imageFile1)
    imageFile1.close()

if __name__ == "__main__":  
    with picamera.PiCamera() as camera:
        camera.start_preview()
        sleep(2)
        camera.stop_preview()
        print "grey-scaled picture"
        takeGrayscaledPicture(camera)
        print "time-lapsed pictures"
        takePictures(camera)
    print "Finished"