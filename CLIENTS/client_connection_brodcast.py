import zmq

def connection_brodcast(port):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://localhost:{port}")
    socket.subscribe("")
    
    return socket