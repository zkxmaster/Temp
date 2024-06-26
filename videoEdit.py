from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

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
                print(f"文件不存在: {file}")
                continue
            
            # 加载视频文件
            clip = VideoFileClip(file)
            clips.append(clip)
        
        except Exception as e:
            print(f"处理文件 {file} 时发生错误: {e}")
    
    if not clips:
        print("没有可处理的视频文件。")
        return
    
    try:
        # 合成视频
        final_clip = concatenate_videoclips(clips)
        
        # 写入合成后的视频文件
        final_clip.write_videofile(output_file, codec='libx264')
        print(f"视频文件成功保存为: {output_file}")
    
    except Exception as e:
        print(f"合成视频时发生错误: {e}")

# 假设你的所有视频文件名保存在一个列表中
video_files = [
    "E:\\FlFile\\中文目录\\ChatGPT.mp4",
    "E:\\FlFile\\中文目录\\Photoshop + AI _ 8大功能，1秒可以解决曾经1天的工作量.mp4"
]

# 调用函数合成视频
merge_videos(video_files, "E:\\FlFile\\中文目录\\output_video.mp4")
