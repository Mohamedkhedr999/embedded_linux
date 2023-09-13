#include <iostream>


int main() {
    int num=0;
    std::cout<<"enter a number: "<<std::endl;
    std::cin>>num;
    auto square= [](int num)->int
    {
        return num * num;


    };
    std::cout<<"square of "<<num<<" = "<<square(num)<<std::endl;


    return 0;
}
