#include<iostream>
using namespace std;

int main(){
    int a[100];
    int num;
    int n=0;
    int t=0;
    cin >> num;
    while (num>0){
        a[n]=num%2;
        num=num/2;
        t++;
        n++;
        
    }
    for (int i=t-1;i>=0;i--){
            cout << a[i] ;
	}
}