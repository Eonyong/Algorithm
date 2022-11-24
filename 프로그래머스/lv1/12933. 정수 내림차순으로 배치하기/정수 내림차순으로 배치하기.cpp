#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    vector<int> num;
    while(n) {
        num.push_back(n % 10);
        n = n / 10;
    };
    sort(num.begin(), num.end());
    reverse(num.begin(), num.end());
    for (int i: num){
        answer = answer * 10 + i;
    }
    return answer;
}