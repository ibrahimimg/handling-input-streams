import cv2

def capture_stream(args):
    ### TODO: Handle image, video or webcam
    input=args.i
    image=False
    #check for live camera feed
    if input.lower()=='cam':
        input=0   
    image_formats=[".png",".jpg",".bmp",".jpeg"]
    for i in range(len(image_formats)):
        # if input is not webcam
        if input==args.i:
            if input.endswith(image_formats[i]):
                input=args.i
                image=True
                break
        else:
            #change it back to webcam
            input=0
    # Get and open video capture
    cap = cv2.VideoCapture(input)
    cap.open(input)
    if not cap.isOpened():
        print("ERROR! Unable to open input source")
        exit(1)
    while cap.isOpened():
        flag,frame=cap.read()
        if not flag:
            break
        key_pressed = cv2.waitKey(60)
        if input==0:
            cv2.imshow("camera",frame)
        elif image:
            cv2.imshow("image",frame)
        else:
            cv2.imshow("video",frame)

        # exit if escape key pressed
        if key_pressed == 27:
                break
        # save current frame if s key pressed
        if key_pressed == ord('s'):
            cv2.imwrite('frame.png',frame)

    #Close the stream and any windows at the end of the application
    cap.release()
    cv2.destroyAllWindows()