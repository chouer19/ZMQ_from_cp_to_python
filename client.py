#client.py
#coding=utf-8  

import zmq

ctx = zmq.Context()

sub2 = ctx.socket(zmq.SUB)
sub2.connect('tcp://localhost:8888')
sub2.setsockopt(zmq.SUBSCRIBE,'')


#for request in range(1,10):
while True:
    message = sub2.recv()
    print 'received reply ','[',message,']'
