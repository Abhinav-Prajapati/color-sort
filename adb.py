from ppadb.client import Client as AdbClient
client = AdbClient()
device = client.device("79dadda0")

def get_screenshrot():
    result = device.screencap()
    with open("screen.png", "wb") as fp:
        fp.write(result)

get_screenshrot()