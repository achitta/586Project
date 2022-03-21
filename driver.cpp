#include "binary_heap.h"
#include "binomial_heap.h"
#include "fibonacci_heap.h"

int main() {
    Heap * binary = new BinaryHeap();
    Heap * binomial = new BinomialHeap();
    Heap * fibonacci = new FibonacciHeap();
    binary->insert(1,2);
    binary->decreaseKey(1,3);
    binary->deleteMin();

    binomial->insert(1,2);
    binomial->decreaseKey(1,3);
    binomial->deleteMin();

    fibonacci->insert(1,2);
    fibonacci->decreaseKey(1,3);
    fibonacci->deleteMin();
    delete binary;
    delete binomial;
    delete fibonacci;
}