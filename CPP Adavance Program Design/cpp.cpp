#include<iostream>

using namespace std;

int main()
{
    long long a, b;
    string c;
    cin >> a >> c >> b;
    if (c == "+"){cout<<a+b;}
    else if (c == "-"){cout<<a-b;}
    else if (c == "*"){cout<<a*b;}
    else if (c == "/"){cout<<a/b;}
}