#include <bits/stdc++.h>

using namespace std;

int main()
{
	long int t;
	cin>>t;
	while(t--)
    {long long n;
    cin >>n;
    n-=1;
    long long i ,count=0;
     for( i=1;i*i<n;i++)
     {
         if (n%i==0)
         {
             count+=2;
         }
     }
    if ( pow(((long long)(sqrt(n))),2)==n)
    {
        count+=1;
            
    }
    cout<<count<<endl;
}
}
        
     
