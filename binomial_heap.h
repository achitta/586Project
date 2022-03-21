#ifndef BINOMIAL_HEAP_H
#define BINOMIAL_HEAP_H

#include "heap.h"

class BinomialHeap : public Heap {
public:
    BinomialHeap();
    ~BinomialHeap();
    void insert(int key, int value);
    int deleteMin();
    void decreaseKey(int key, int newValue);
};

#endif