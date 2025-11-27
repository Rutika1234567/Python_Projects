import time
from plyer import notification
# C:/Users/Rutika/AppData/Local/Programs/Python/Python314/python.exe -m pip install plyer

while True:
    print("Please sip some water!")
    notification.notify(
        title="please drink some water",
        message="You need to drink")

    time.sleep(1800)   # this is in second 
