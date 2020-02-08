import io
import picamera
from PIL import Image

class img_task:

	def __init__(self):
		self.camera = None
		self.im = None

	def open(self):
		self.camera = picamera.PiCamera()
		camera.resolution(480, 480)
		camera.framerate(60)
		time.sleep(1)

	def read(self):
		self.open()
		try:
			camera.capture_sequence(self.output(), 'jpeg', use_video_port=True)
			return self.im, True
		except:
			return '', False

	def output(self):
		stream = io.BytesIO()
		yield stream
		self.im = Image.open(stream)
		stream.seek(0)
		stream.truncate()

	def __str__(self):
        	return f"Camera exists"
