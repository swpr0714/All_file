#include<iostream>
using namespace std;

int main(){
    int x;
    while (cin>>x){
        int n=0;
        while(x!=1){
            if (x%2==1){
                x=x*3+1;
                n++;
            }
            else{
                x/=2;
                n++;
            }
        }
        cout<<n<<endl;
    }
}