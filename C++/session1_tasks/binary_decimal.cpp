#include <iostream>
#include <bitset>
#include <string>

// Function to convert decimal to binary
std::string decimalToBinary(int decimal) {
    return std::bitset<32>(decimal).to_string();
}

// Function to convert binary to decimal
int binaryToDecimal(const std::string& binary) {
    return std::bitset<32>(binary).to_ulong();
}

int main() {
    int decimalNumber = 0;
    std::string binary_num;
    std::cout<<"enter a decimal number :" << std::endl;
    std::cin >> decimalNumber;
    std::cout<<"enter a binary number :" << std::endl;
    std::cin >> binary_num;
    

    // Convert decimal to binary
    std::string convertedBinary = decimalToBinary(decimalNumber);
    std::cout << "Decimal " << decimalNumber << " in binary: " << convertedBinary << std::endl;

    // Convert binary to decimal
    int convertedDecimal = binaryToDecimal(binary_num);
    std::cout << "Binary " << binary_num << " in decimal: " << convertedDecimal << std::endl;

    return 0;
}
