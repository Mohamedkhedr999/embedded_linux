#include <iostream>
#include <iomanip>
//#include <ostream>


int main()
{
   int num1 = 0,num2 = 0,num3 = 0;


    std::cout << "enter 3 integers" << std::endl;
    std::cin >>num1 >> num2 >> num3;
    

    if(num1 > num2 && num1 > num3)
    {
        std::cout << " the maximux number is num1 = "<< num1 <<std::endl;
    }
    else if(num2 > num1 && num2 > num3)
    {
        std::cout << " the maximux number is num2 = "<< num2 <<std::endl;
    }
    else if(num2 > num1 && num2 > num3)
    {
        std::cout << " the maximux number is num3 = "<< num3 <<std::endl;

    }
    else
    {
        std::cout << " all numbers are equal"<<std::endl;
        
    }
   
}