#include<iostream>

using namespace std;

int main()
{
    int x, y, i;
    cin >> x >> y;
    while (x!=0&&y!=0)
    {
        if (x>=y){
            x=x%y;
        }
        else
        {
            y=y%x;
        }
    }
    if (x==0){cout<<y;}
    if (y==0){cout<<x;}
}