#include "binary_heap.h"
#include <iostream>

using namespace std;

BinaryHeap::BinaryHeap() {
    cout << "Binary constructor" << endl;
}

BinaryHeap::~BinaryHeap() {
    cout << "Binary destructor" << endl;
}

void BinaryHeap::insert(int key, int value) {
    cout << "Binary insert" << endl;
}

void BinaryHeap::decreaseKey(int key, int newValue) {
    cout << "Binary decrease" << endl;
}

int BinaryHeap::deleteMin() {
    cout << "Binary delete" << endl;
    return 0;
}