import cv2, pyvirtualcam, os, configparser


# Variables
file = 'config.ini'
section = 'IPCamera'

config = configparser.ConfigParser()


# Default Config
if not os.path.isfile(file):
    config.read(file)
    config.add_section(section)

    config.set(section, 'ip', '192.168.1.16:8080')
    config.set(section, 'width', '1920')
    config.set(section, 'height', '1080')
    config.set(section, 'fps', '30')

    with open('config.ini', 'w') as f:
        config.write(f)


# Read Config
config.read(file)

ip = config.get(section, 'ip')
width = config.getint(section, 'width')
height = config.getint(section, 'height')
fps = config.getint(section, 'fps')


# Open Camera
with pyvirtualcam.Camera(width=width, height=height, fps=fps, device="IPCamera") as vcam:

    print(f'Virtual cam started: {vcam.device} ({vcam.width}x{vcam.height} @ {vcam.fps}fps)')

    ipcam = cv2.VideoCapture(0)
    address = "http://" + ip + "/video"
    ipcam.open(address)

    while ipcam.isOpened():
        ret, frame = ipcam.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        vcam.send(img)
        vcam.sleep_until_next_frame()

    ipcam.release()
    cv2.destroyAllWindows()