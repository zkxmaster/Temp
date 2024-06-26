import os
import time
import json
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 配置日志
logging.basicConfig(
    filename='video_file_watcher.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".flv"}
WATCH_DIRECTORY = "E:\\FlFile\\"

class VideoFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and self.is_video_file(event.src_path):
            self.log_file_info("新增", event.src_path)

    def on_modified(self, event):
        if not event.is_directory and self.is_video_file(event.src_path):
            self.log_file_info("修改视频文件", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory and self.is_video_file(event.src_path):
            self.log_file_info("删除", event.src_path, file_deleted=True)

    @staticmethod
    def is_video_file(file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower() in VIDEO_EXTENSIONS

    @staticmethod
    def log_file_info(event_type, file_path, file_deleted=False):
        try:
            file_size = 0 if file_deleted else os.path.getsize(file_path)
            file_info = {
                "事件类型": event_type,
                "文件路径": file_path,
                "文件名": os.path.basename(file_path),
                "文件大小": file_size
            }
            logging.info(json.dumps(file_info, ensure_ascii=False, indent=4))
        except Exception as e:
            logging.error(f"处理文件 {file_path} 时出错: {e}")

if __name__ == "__main__":
    try:
        event_handler = VideoFileHandler()
        observer = Observer()
        observer.schedule(event_handler, path=WATCH_DIRECTORY, recursive=True)

        logging.info(f"开始监控目录: {WATCH_DIRECTORY}")
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()
    except Exception as e:
        logging.error(f"启动监控器时出错: {e}")
