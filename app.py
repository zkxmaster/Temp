from gradio_client import Client, file

client = Client("http://192.168.120.52:7860/")
result = client.predict(
		video_input={"video":file('C:\\Users\\zkxmaster\\Downloads\\PSAI.mp4')},
		audio_input=file('C:\\Users\\zkxmaster\\Downloads\\PSAI.mp4'),
		hotwords="",
		output_dir=" ",
		api_name="/mix_recog"
)
print(result)