#include <iostream>
#include <algorithm>

#define NOTFOUND  -1
// Function to search for a number in an array c style
/*int  searchNumber(int arr[], int size, int number) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == number) {
            return i; // Number found in the array
        }
    }
    return NOTFOUND; // Number not found in the array
}*/

int main() {
 

    int arr[] = {1,5,4,88,6,20,10,4,7,2,0};
    int size = sizeof(arr)/sizeof(arr[0]);
  // int arr[] = {5, 3, 7, 6, 8, 2};
    int target = 6;
 
    //int n = sizeof(arr) / sizeof(*arr);
 
    int *i = std::find(arr, arr + size, target) ;
    if(i-arr < size)
    {
        std::cout <<"found at " <<(i-arr)<<std::endl;

    }
    else
    {
        std::cout <<"Not found  "<<std::endl;

    }
    
    
    
 
    return 0;

  /*  int number;
    std::cout << "Enter the number to search for: ";
    std::cin >> number;
    int index = searchNumber(arr, size, number);
    if (index != NOTFOUND) {
        std::cout << "Number found in the array in index:"<< index << std::endl;
    } else {
        std::cout << "Number not found in the array." << std::endl;
    }

    return 0;*/
}
