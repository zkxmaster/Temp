import os
import logging
from moviepy.editor import VideoFileClip, concatenate_videoclips

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def merge_videos(video_files, output_file):
    """
    合成多个视频文件为一个视频文件。

    参数：
    video_files (list of str): 视频文件路径列表。
    output_file (str): 输出视频文件路径。
    """
    clips = []
    for file in video_files:
        try:
            # 检查文件是否存在
            if not os.path.exists(file):
                logging.warning(f"文件不存在: {file}")
                continue
            
            # 加载视频文件
            clip = VideoFileClip(file)
            clips.append(clip)
        
        except Exception as e:
            logging.error(f"处理文件 {file} 时发生错误: {e}")
    
    if not clips:
        logging.warning("没有可处理的视频文件。")
        return
    
    try:
        # 合成视频
        final_clip = concatenate_videoclips(clips)
        
        # 写入合成后的视频文件
        final_clip.write_videofile(output_file, codec='libx264', verbose=False)
        logging.info(f"视频文件成功保存为: {output_file}")
    
    except Exception as e:
        logging.error(f"合成视频时发生错误: {e}")

# 假设你的所有视频文件名保存在一个列表中
video_files = [
    os.path.join("E:", "FlFile", "中文目录", "ChatGPT.mp4"),
    os.path.join("E:", "FlFile", "中文目录", "Photoshop + AI _ 8大功能，1秒可以解决曾经1天的工作量.mp4")
]

# 调用函数合成视频
merge_videos(video_files, os.path.join("E:", "FlFile", "中文目录", "output_video.mp4"))