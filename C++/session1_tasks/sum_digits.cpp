#include <iostream>

int main() {
    int number, sum = 0;

    std::cout << "Enter an integer: ";
    std::cin >> number;

    // Calculate the sum of digits
    while (number != 0) {
        sum += number % 10;  // Add the last digit to the sum
        number /= 10;       // Remove the last digit from the number
    }

    std::cout << "Sum of the digits: " << sum << std::endl;

    return 0;
}
