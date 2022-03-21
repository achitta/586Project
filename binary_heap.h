#ifndef BINARY_HEAP_H
#define BINARY_HEAP_H

#include "heap.h"

class BinaryHeap : public Heap {
public:
    BinaryHeap();
    ~BinaryHeap();
    void insert(int key, int value);
    int deleteMin();
    void decreaseKey(int key, int newValue);
};

#endif