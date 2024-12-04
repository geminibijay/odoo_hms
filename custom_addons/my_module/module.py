from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File {event.src_path} has been modified.')

def start_file_observer():
    path = r'C:\Users\sbijay\Desktop\odoo\custom_addons'  # Replace with the directory to monitor
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start the file observer in a separate thread
threading.Thread(target=start_file_observer, daemon=True).start()
