#include <iostream>


int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Even numbers: ";
    for (int i = 0; i < size; i++) {
        if (!(arr[i] & 1)) {
            std::cout << arr[i] << " ";
        }
    }

    std::cout << "\nOdd numbers: ";
    for (int i = 0; i < size; i++) {
        if (arr[i] &1) {
            std::cout << arr[i] << " ";
        }
    }
    std::cout<<std::endl;


    return 0;
}
