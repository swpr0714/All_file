#include<iostream>
using namespace std;

int main(){
    int n,m;
    while (cin>>n>>m){
        long long pow=1;
        long long facn=n;
        long long facm=m;
        if (n==0){facn=1;}
        if (m==0){facm=1;}
        for (int i=0;i<m;i++){pow =pow*n;}
        while (n>1){
            n--;
            facn = facn*n;
        }
        while (m>1){
            m--;
            facm = facm*m;
        }
        long long ans =facn/facm;
        cout<<ans+pow<<endl;
    }
}