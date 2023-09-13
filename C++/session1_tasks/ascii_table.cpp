#include <iostream>
#include <iomanip>

int main()
{
   
    std::cout << "ASCII  |   char" << std::endl;
    for(unsigned char i = 0; i < 128; i++)
    {
        std::cout << std::setw(3)  <<static_cast<int> (i) << "    |   "<<i << std::endl;
    }
    return 0;
}
