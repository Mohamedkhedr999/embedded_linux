#include "iostream"


int main()
{
    char l = 0;
    std::cout << "enter a letter"<< std::endl;
    std::cin >> l;
    l = tolower(l);
    if(l == 'a' || l == 'e' || l == 'o' || l == 'i' || l == 'u')
    {
        std:: cout << "this char "<< l << " is vowel"<< std::endl;
    }
    else
    {
        std:: cout << "this char "<< l << " is not vowel"<< std::endl;

    }






}