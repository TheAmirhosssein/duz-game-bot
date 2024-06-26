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
        if event.src_path == os.path.abspath(self.script_path):
            print(f"{self.script_path} modified; restarting...")
            self.start_script()


if __name__ == "__main__":
    script_path = "app/bot.py"

    event_handler = ChangeHandler(script_path)
    observer = Observer()
    observer.schedule(
        event_handler,
        path=os.path.dirname(os.path.abspath(script_path)),
        recursive=False,
    )
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
