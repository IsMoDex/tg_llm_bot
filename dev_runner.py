import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCHED_EXTENSIONS = ('.py',)


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, start_fn):
        self.start_fn = start_fn

    def on_any_event(self, event):
        if event.src_path.endswith(WATCHED_EXTENSIONS):
            print(f"🔄 Изменения обнаружены: {event.src_path}")
            self.start_fn(restart=True)


class BotRunner:
    def __init__(self):
        self.process = None

    def start(self, restart=False):
        if self.process:
            self.process.terminate()
            self.process.wait()
            print("🚫 Старый процесс остановлен.")

        print("🚀 Запуск бота...")
        self.process = subprocess.Popen([sys.executable, "bot.py"])

    def run(self):
        event_handler = ChangeHandler(self.start)
        observer = Observer()
        observer.schedule(event_handler, ".", recursive=True)
        observer.start()

        try:
            self.start()
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            if self.process:
                self.process.terminate()
        observer.join()


if __name__ == "__main__":
    runner = BotRunner()
    runner.run()
