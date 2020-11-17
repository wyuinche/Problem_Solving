#include <iostream>
#include <algorithm>
using namespace std;

int n;
int map[25][25];
int mark[25][25];
int result[400];

void marking(int i, int j, int num);

int main(void){
    int i, j;
    int curr=0;
    cin>>n;

    for(i=0; i<n; i++)
        for(j=0; j<n; j++){
             scanf("%1d", &map[i][j]);
            mark[i][j]=-1;
        }
    for(i=0; i<400; i++)
        result[i]=0;

    for(i=0; i<n; i++){
        for(j=0;j<n;j++){
            if(map[i][j]!=0&&mark[i][j]==-1){
                curr++;
            }
            marking(i, j, curr);
        }
    }
    
    cout<<curr<<endl;
    sort(result+1, result+curr+1);
    for(i=1; i<=curr; i++)
        cout<<result[i]<<endl;

    return 0;
}

void marking(int i, int j, int num){
    if(mark[i][j]!=-1||i<0||i>=n||j<0||j>=n)
        return;
    else if(map[i][j]==0){
        mark[i][j]=0;
    }
    else if(map[i][j]==1){
        mark[i][j] = num;
        result[num]++;
        marking(i-1, j, num);
        marking(i+1, j, num);
        marking(i, j-1, num);
        marking(i, j+1, num);
    }
}