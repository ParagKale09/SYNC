from plyer import notification
title = 'STUDY Alert....'
message = 'Its time to study!!!'

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)

"""
from plyer import notification
if __name__ == '__main__':
        notification.notify(
            title = "**Please Drink Water Now!!",
            message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "D:\KOKP\Internship\Projects\SYNC Python\Desktop Notifier\icon.ico",
            timeout= 6
            )
"""
