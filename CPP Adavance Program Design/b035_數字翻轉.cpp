#include<iostream>
using namespace std;

int main(){
    int a;
    while (cin>>a){
        int ts=0;
        while(a>0){
            ts*=10;
            ts+=a%10;
            a/=10;
        }
        cout<<ts<<endl;
    }
}