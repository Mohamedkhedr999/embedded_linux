# import pynotifier
# import psutil

# battery =psutil.sensors_battery()

# percent = battery.percent
# print(percent)
# #pynotifier.Notification("battery precentage", str(percent) + "%percent remaining", duration = 10).send()

# pynotifier.Notification("Battery Percentage", str(percent) + "% remaining", title="Battery Status", duration=10)
# #pynotifier.notify(title="Battery Status", message=str(percent) + "% remaining", timeout=10)
from plyer import notification
import psutil

battery = psutil.sensors_battery()
percent = battery.percent
print(percent)
notification.notify(title="Battery Status", message=str(percent) + "% remaining", timeout=10)
