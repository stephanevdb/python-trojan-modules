import webbrowser
import time
url = "https://svdb.cc/r"

for i in range(0, 10):
    webbrowser.open(url, new=0, autoraise=True)
    time.sleep(10)
