#include <iostream>
using namespace std;
int main(){
//    std::ios_base::sync_with_stdio(false);
    int i, ln, A[4] ;
    cin >> ln;
    i=0;
    while(i<ln){
        i++;
        for(int i=0; i<4; i++){
            cin >> A[i];
        }
        if ((A[3]-A[2])==(A[2]-A[1]) && (A[2]-A[1])==(A[1]-A[0])){
            cout <<A[0]<<" "<<A[1]<<" "<<A[2]<<" "<<A[3]<<" "<<2*A[3]-A[2]<<endl;
        }
        else{
            cout <<A[0]<<" "<<A[1]<<" "<<A[2]<<" "<<A[3]<<" "<<A[3]*A[3]/A[2]<<endl;
        }
    }
}