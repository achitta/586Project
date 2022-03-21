#ifndef FIBONACCI_HEAP_H
#define FIBONACCI_HEAP_H

#include "heap.h"

class FibonacciHeap : public Heap {
public:
    FibonacciHeap();
    ~FibonacciHeap();
    void insert(int key, int value);
    int deleteMin();
    void decreaseKey(int key, int newValue);
    void getMin();
};

#endif