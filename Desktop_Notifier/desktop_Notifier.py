from plyer import notification
title = 'STUDY Alert....'
message = 'Its time to study!!!'

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
