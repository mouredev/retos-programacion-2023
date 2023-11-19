#include <bits/stdc++.h>

#define lli long long int
#define endL '\n'

using namespace std;

void terna(lli);
bool mcd(lli,lli);

int main() {
    lli n;
    cin>>n;
    terna(n);
    return 0;
    }

bool mcd(lli p, lli q) {
    lli resp;
    do {
        resp = q;
        q = p%q;
        p = resp;
        }
    while(q!=0);
    if(resp==1)
        return 1;
    else
        return 0;
    }

void terna(lli maxi) {
    lli p(2),q(1),a((p*p)-(q*q)),b(2*p*q),c((a*a)+(b*b)),i,j;
    c = sqrt(c);
    while(c<=maxi) {
        i=1;
        while(c*i<=maxi) {
        if(a<b) {
            cout<<"("<<a*i<<", ";
            cout<<b*i<<", ";
            }
        else {
            cout<<"("<<b*i<<", ";
            cout<<a*i<<", ";
            }
        cout<<c*i<<")"<<endL;
        i++;
        }
        j=0;
        do {
            q++;
            if(p==q) {
                p++;
                q=1;
                j++;
                }
            while((mcd(p,q)==0) || ((p%2==1 && q%2==1) || (p%2==0 && q%2==0)))
                q++;
            a=(p*p)-(q*q);
            b=2*p*q;
            c= sqrt((a*a)+(b*b));
            }
        while(c>maxi && j<=1);
        }
    }
