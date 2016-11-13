#!/usr/bin/python

import dropbox
import cv2
import time
import yaml


"""
Function to take a frame. This allows the camera to stay off most of the time, by only opening it when needed, and releasing it later. The 'prepFrames' parameter defines how many frames will be captured and discarded before the actual saved frame.
"""
def getFrame(cam, filename, prepFrames=15):
    cam.open(0)
    [cam.read() for i in range(0, prepFrames)]
    img = cam.read()
    cv2.imwrite(filename, img[1])
    cam.release()

def main():
    print "Reading config..."

    with open("config.yml", "r") as ymlfile:
        config = yaml.load(ymlfile)
    
    print "Connecting to Dropbox..."

    # Set up dropbox connection to be maintained
    client = dropbox.client.DropboxClient(config['api_key'])

    print "Connected to {} on Dropbox".format(client.account_info()['email'])
    print "Initializing camera..."

    # Set up camera system

    cam = cv2.VideoCapture()
    prep_frames = int(config['prep_frames'])
    filename = config['frame_filename']
    sleep_seconds = config['sleep_seconds']
    
    print "Initialization complete!"

    while True:
        getFrame(cam, filename, prep_frames)
        fileToUpload = open(filename, "rb")
        response = client.put_file("/{}".format(filename), fileToUpload, overwrite=True)
        print "Uploaded frame: ", (response is not None)
        fileToUpload.close()
        
        time.sleep(sleep_seconds)


if __name__ == "__main__":
    main()
