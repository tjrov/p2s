from tasks.ethernet import ethernet_task
from tasks.img import img_task
from tasks.fc import fc_task
from tasks.imu import imu_task

class main_control_loop:

	def __init__(self):
		self.ethernet_t: ethernet_task = ethernet_task()
		self.img_t: img_task = img_task()
		self.fc_t: fc_task =  fc_task()
		self.imu_t: imu_task = imu_task()


	def execute(self):
		# READ BLOCK
		eth_message = self.ethernet_t.read() #read ethernet message
		image = self.img_t.read() #read image from camera
		imu_data = self.imu_t.read()

		# ACTUATE BLOCK
		self.fc_t.actuate(eth_message) #send command to flight controller
		self.ethernet_t.actuate([image, imu_data]) #send ethernet message
