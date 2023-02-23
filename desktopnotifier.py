from plyer import notification
import time

while True:
    notification.notify(
        title = 'Alert!!',
        message = 'Its time to study!!',
        timeout = 5,
    )
    time.sleep(5)
    quit()