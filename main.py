import argparse
import cv2
import capture

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "location of the input file or use cam for webcam"
    # -- Create the arguments
    parser.add_argument("-i", help=i_desc,required=True)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    capture.capture_stream(args)

if __name__ == "__main__":
    main()