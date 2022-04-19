#include<iostream>
using namespace std;

int main(){
    string a;
    while (cin>>a){
        int len = a.length();
        if (a[0]==a[len-1]){
            cout<<"yes"<<endl;
        }
        else{
            cout<<"no"<<endl;
        }
    }
}