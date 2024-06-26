import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".flv"}
WATCH_DIRECTORY = "E:\\FlFile\\"

class VideoFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and self.is_video_file(event.src_path):
            self.print_file_info("新增", event.src_path)

    # def on_modified(self, event):
    #     if not event.is_directory and self.is_video_file(event.src_path):
    #         self.print_file_info("修改视频文件", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory and self.is_video_file(event.src_path):
            self.print_file_info("删除", event.src_path, file_deleted=True)

    @staticmethod
    def is_video_file(file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower() in VIDEO_EXTENSIONS

    @staticmethod
    def print_file_info(event_type, file_path, file_deleted=False):
        try:
            file_size = 0 if file_deleted else os.path.getsize(file_path)
            file_info = {
                "event_type": event_type,
                "file_path": file_path,
                "file_name": os.path.basename(file_path),
                "file_size": file_size
            }
            print(json.dumps(file_info, ensure_ascii=False, indent=4))
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    try:
        event_handler = VideoFileHandler()
        observer = Observer()
        observer.schedule(event_handler, path=WATCH_DIRECTORY, recursive=True)

        print(f"开始监控目录: {WATCH_DIRECTORY}")
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()
    except Exception as e:
        print(f"Error starting watcher: {e}")
