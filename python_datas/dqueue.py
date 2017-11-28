# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:29:38 2017

@author: huhuy
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:43:41 2017

@author: huhuy
"""

"""Queue represented by a pseudo stack (represented by a list with pop and append)"""
class QueueOnStack():
    def __init__(self):
        self.stack = []
        self.length = 0

    def __str__(self):
        printed = '<' + str(self.stack)[1:-1] + '>'
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""
    def put(self, item):
        self.stack.append(item)
        self.length = self.length + 1

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""
    def get(self):
        self.rotate(1)
        dequeued = self.stack[self.length-1]
        self.stack = self.stack[:-1]
        self.rotate(self.length-1)
        self.length = self.length -1
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""
    def rotate(self, rotation):
        for i in range(rotation):
            temp = self.stack[0]
            self.stack = self.stack[1:]
            self.put(temp)
            self.length = self.length - 1

    """Reports item at the front of self
    @return item at front of self.stack"""
    def front(self):
        front = self.get()
        self.put(front)
        self.rotate(self.length-1)
        return front

    """Returns the length of this.stack"""
    def size(self):
        return self.length
    
if __name__ == '__main__':
    ques=QueueOnStack()
    ques.put('ac')
    ques.put("56")
    ques.put('po')
    ques.put('re')
    #ques.rotate(2)
    print("gue get:"+str(ques.get())+"  :: "+ str(ques.size()))