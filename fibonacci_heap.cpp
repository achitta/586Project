#include "fibonacci_heap.h"
#include <iostream>

using namespace std;

FibonacciHeap::FibonacciHeap() {
    cout << "Fibonacci constructor" << endl;
}

FibonacciHeap::~FibonacciHeap() {
    cout << "Fibonacci destructor" << endl;
}

void FibonacciHeap::insert(int key, int value) {
    cout << "Fibonacci insert" << endl;
}

void FibonacciHeap::decreaseKey(int key, int newValue) {
    cout << "Fibonacci decrease" << endl;
}

int FibonacciHeap::deleteMin() {
    cout << "Fibonacci delete" << endl;
    return 0;
}