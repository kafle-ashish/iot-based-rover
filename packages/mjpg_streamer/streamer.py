import os

def stream(fps=5, res=[480, 320]):
    STREAMER_PATH = "/home/pi/Documents/minor_prj/git/iot-based-rover/packages/mjpg_streamer"
    PATH = os.getcwd()
    if(PATH != STREAMER_PATH):
        os.chdir(STREAMER_PATH)
    #print(PATH)
    os.system('sudo mjpg_streamer -i "./input_uvc.so -f {0} -r {1}x{2} -n -y" -o "./output_http.so -w ./www -p 80"'.format(fps, res[0], res[1]))
    return

if __name__ == "__main__":
    stream()
