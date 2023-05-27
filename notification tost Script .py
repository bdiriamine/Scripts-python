#pip install win10toast
from win10toast import ToastNotifier
toast_notifier = ToastNotifier()

toast_notifier.show_toast(
    'exmple',
    'welcome bdiri',
    icon_path=None,
    duration=10,
    threaded=True
)