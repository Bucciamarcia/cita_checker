import platform
import subprocess
from plyer import notification
from py.shared.logger import get_logger


class AlertHandler:
    def __init__(self, app_name="Cita Checker", timeout=10):
        self.app_name = app_name
        self.timeout = timeout
        self.current_os = platform.system()
        self.logger = get_logger(__name__)

    def show_notification(self, title, message):
        if self.current_os == "Linux":
            self._notify_linux(title, message)
        elif self.current_os == "Darwin":
            self._notify_mac(title, message)
        elif self.current_os == "Windows":
            self._notify_windows(title, message)
        else:
            self.logger.error(f"Unsupported OS: {self.current_os}")

    def _notify_linux(self, title, message):
        try:
            subprocess.run(["notify-send", title, message])
        except FileNotFoundError:
            self.logger.error("notify-send not found. Please install libnotify-bin.")

    def _notify_mac(self, title, message):
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script])
        except FileNotFoundError:
            self.logger.error("osascript not found.")

    def _notify_windows(self, title, message):
        try:
            notification.notify(
                title=title,
                message=message,
                app_name=self.app_name,
                timeout=self.timeout,
            )
        except Exception as e:
            self.logger.error(f"Error showing notification: {e}")
