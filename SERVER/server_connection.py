import zmq

def connection():
    context = zmq.Context()
    socket1 = context.socket(zmq.REP)
    socket1.bind("tcp://*:5555")
    
    return socket1
