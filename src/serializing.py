from zmq import Socket, Context 

import numpy as np
    
class SerializingSocket(Socket):
    
    def send_array(self, A, msg='NoName', flags=0, copy=True, track=False):
        
        md = dict( msg = msg, dtype = str(A.dtype), shape = A.shape, )
        
        self.send_json(md, flags | zmq.SNDMORE)
        return self.send(A, flags, copy=copy, track=track)

    def send_jpg(self, msg='NoName', jpg_buffer=b'00', flags=0, copy=True, track=False):
        
        md = dict(msg = msg) # i dont know
        
        self.send_json(md, flags | zmq.SNDMORE)
        return self.send(jpg_buffer, flags, copy=copy, track=track)

    def recv_array(self, flags=0, copy=True, track=False):    
        
        md = self.recv_json(flags=flags)
        msg = self.recv(flags=flags, copy=copy, track=track)
        
        A = np.frombuffer(msg, dtype=md['dtype'])
        return (md['msg'], A.reshape(md['shape']))

    def recv_jpg(self, flags=0, copy=True, track=False):
        md = self.recv_json(flags=flags)  # metadata text
        jpg_buffer = self.recv(flags=flags, copy=copy, track=track)
        return (md['msg'], jpg_buffer)

class SerializingContext(zmq.Context):
    _socket_class = SerializingSocket