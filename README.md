# Dogmon - Webcam based monitoring script

## Purpose
For monitoring what dogs do while people are away.

## How to use
Edit the config.yml file to include a valid Dropbox API key, which you can generate from the [apps dashboard](https://www.dropbox.com/developers/apps).

Hook up any kind of camera, as long as OpenCV is able to see it.

Run with `./dogmon.py`. You may stop the application with ctrl+c.

The application will immediately connect to Dropbox and initialize a camera connection.
Every `sleep_seconds` seconds, it will take a snapshot and upload to `frame_filename` in your app folder on Dropbox.
Create a public link to this file, and you will have a semi-live feed to your camera.

Increasing `prep_frames` setting may give you better image quality, depending on the camera.
Many cameras need to warm up before they can properly capture anything, by detecting lighting, etc.
This setting controls how many frames are pulled and discarded from the camera before capturing the final frame to upload.
For me, 15 was the highest neccessary.
