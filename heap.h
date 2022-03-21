#ifndef HEAP_H
#define HEAP_H

class Heap {
public:
    Heap();
    virtual ~Heap();
    virtual void insert(int key, int value) = 0;
    virtual int deleteMin() = 0;
    virtual void decreaseKey(int key, int newValue) = 0; 
    virtual void getMin() = 0;
};

#endif