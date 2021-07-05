import zmq
import numpy as np

from .serializing import SerializingContext

class ImageSender():
    
	def __init__(self, 
              	connect_to='tcp://127.0.0.1:5555', 
                REQ_REP = True):
     
		if REQ_REP == True: 
      		# REQ/REP mode, this is a blocking scenario
			self.init_reqrep(connect_to)
		else: 
      		#PUB/SUB mode, non-blocking scenario
			self.init_pubsub(connect_to)

	def init_reqrep(self, address): 
     	#Creates and inits a socket in REQ/REP mode
		socketType = zmq.REQ
		self.zmq_context = SerializingContext() # this is a key
		self.zmq_socket = self.zmq_context.socket(socketType)
		self.zmq_socket.connect(address)
		# Assign corresponding send methods for REQ/REP mode
		self.send_image = self.send_image_reqrep
		self.send_jpg   = self.send_jpg_reqrep

	def init_pubsub(self, address): #Creates and inits a socket in PUB/SUB mode
		socketType = zmq.PUB
		self.zmq_context = SerializingContext() # this is a key
		self.zmq_socket = self.zmq_context.socket(socketType)
		self.zmq_socket.bind(address)
		# Assign corresponding send methods for PUB/SUB mode
		self.send_image = self.send_image_pubsub
		self.send_jpg   = self.send_jpg_pubsub

	def send_image(self, msg, image):
		""" This is a placeholder. This method will be set to either a REQ/REP
		or PUB/SUB sending method, depending on REQ_REP option value.
		Arguments:
			msg: text message or image name.
			image: OpenCV image to send to hub.
		Returns:
			A text reply from hub in REQ/REP mode or nothing in PUB/SUB mode.
		"""
		pass

	def send_image_reqrep(self, msg, image):
		if image.flags['C_CONTIGUOUS']: 
      		# if image is already contiguous in memory just send it
			self.zmq_socket.send_array(image, msg, copy=False)
		else: # else make it contiguous before sending
			image = np.ascontiguousarray(image)
			self.zmq_socket.send_array(image, msg, copy=False)
		hub_reply = self.zmq_socket.recv()  # receive the reply message
		return hub_reply

	def send_image_pubsub(self, msg, image):
		if image.flags['C_CONTIGUOUS']: # if image is already contiguous in memory just send it
			self.zmq_socket.send_array(image, msg, copy=False)
		else: # else make it contiguous before sending
			image = np.ascontiguousarray(image)
			self.zmq_socket.send_array(image, msg, copy=False)

	def send_jpg(self, msg, jpg_buffer):
		"""This is a placeholder. This method will be set to either a REQ/REP
		or PUB/SUB sending method, depending on REQ_REP option value.
		Arguments:
			msg: image name or message text.
			jpg_buffer: bytestring containing the jpg image to send to hub.
		Returns:
			A text reply from hub in REQ/REP mode or nothing in PUB/SUB mode.
		"""
		pass

	def send_jpg_reqrep(self, msg, jpg_buffer):
		self.zmq_socket.send_jpg(msg, jpg_buffer, copy=False)
		hub_reply = self.zmq_socket.recv()  # receive the reply message
		return hub_reply

	def send_jpg_pubsub(self, msg, jpg_buffer):
		
		self.zmq_socket.send_jpg(msg, jpg_buffer, copy=False)

	def close(self):
		# Closes the ZMQ socket and the ZMQ context.
		self.zmq_socket.close()
		self.zmq_context.term()

	def __enter__(self):
		# Enables use of ImageSender in with statement. Returns: self.
		return self

	def __exit__(self, exc_type, exc_val, exc_tb): 
		# Enables use of ImageSender in with statement.
		self.close()