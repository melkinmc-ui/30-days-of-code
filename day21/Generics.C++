#include <iostream>
#include <vector>
#include <string>

using namespace std;
template <typename T>
void printArray(const vector<T>& vec) {
    for (const auto& item : vec) {
        cout << item << endl;
    }
}
/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here

int main() {