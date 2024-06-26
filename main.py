import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable, self.script_path])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} modified; restarting...")
            self.start_script()


if __name__ == "__main__":
    package_directory = "apps"

    script_path = os.path.join(package_directory, "bot.py")

    event_handler = ChangeHandler(script_path)
    observer = Observer()
    observer.schedule(
        event_handler, path=os.path.abspath(package_directory), recursive=True
    )
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
