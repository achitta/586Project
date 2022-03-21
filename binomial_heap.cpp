#include "binomial_heap.h"
#include <iostream>

using namespace std;

BinomialHeap::BinomialHeap() {
    cout << "Binomial constructor" << endl;
}

BinomialHeap::~BinomialHeap() {
    cout << "Binomial destructor" << endl;
}

void BinomialHeap::insert(int key, int value) {
    cout << "Binomial insert" << endl;
}

void BinomialHeap::decreaseKey(int key, int newValue) {
    cout << "Binomial decrease" << endl;
}

int BinomialHeap::deleteMin() {
    cout << "Binomial delete" << endl;
    return 0;
}

void BinomialHeap::getMin() {
    cout << "Binomial get" << endl;
}