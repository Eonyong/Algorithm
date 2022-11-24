#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;
    while (true) {
        answer += n % 10;
        n = int(n / 10);
        if (n <= 0) return answer;
    }

    
}