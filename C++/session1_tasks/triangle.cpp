#include <iostream>
//#include <ostream>


int main()
{
    int num=0;
    std::cout << "enter the height of the triangle:" << std:: endl ;

    std::cin >> num;
   for(signed int i = num-1; i >= 0; i--)
   {

    for(int j = 0; j < num;j++)
    {
        if(j >= i)
        {
            std::cout << "*";
        }
        else
        {
            std::cout<<" ";
        }
    }
    std::cout << std::endl;

   }
}