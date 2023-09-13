#include <iomanip>
#include <iostream>



int main()
{
    for(int i = 1; i <= 12; i++ )
    {
        for (int j = 1; j <= 12; j++) 
        {
            //std::cout<<i<<std::setw(3)<<" x "<<j<<std::setw(3)<<"=" << i*j<<std::setw(3)<<std::endl ;
           std::cout<<std::setw(3)<<i<<" x "<<std::setw(3)<<j<<" = " << i*j<<std::setw(3)<<std::endl ;
        }
    }
}