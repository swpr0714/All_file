#include<iostream>
using namespace std;

int main(){
    string a;
    while (cin>>a){
        int len = a.length();
        for (int i=0;i<len/2;i++){
            if (a[i]==a[len-i-1]){
                 
            }
            else{
                cout<<"no";
                return 0;
            }
            cout<<"yes";
        }
    }
}