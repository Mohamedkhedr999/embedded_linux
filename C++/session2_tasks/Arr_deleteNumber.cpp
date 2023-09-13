#include <iostream>

void deleteNumber(int arr[], int& size, int numberToDelete)
{
    int i, j;
    bool found = false;

    // Find the number to delete in the array
    for (i = 0; i < size; i++) 
    {
        if (arr[i] == numberToDelete) {
            found = true;
            break;
        }
    }

    // If the number is found, delete it by shifting the elements
    if (found)
    {
        for (j = i; j < size - 1; j++) 
        {
            arr[j] = arr[j + 1];
        }
        size--; // Decrease the size of the array
        std::cout << "Number deleted successfully." << std::endl;
    } else {
        std::cout << "Number not found in the array." << std::endl;
    }
}

int main() 
{
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    int numberToDelete;

    std::cout << "Enter the number to delete: ";
    std::cin >> numberToDelete;

    deleteNumber(arr, size, numberToDelete);

    std::cout << "Updated array: ";
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
