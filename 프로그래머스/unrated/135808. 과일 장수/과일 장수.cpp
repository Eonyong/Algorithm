#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    sort(score.begin(), score.end(), greater<>());
    for (int i = 0; i < score.size(); i += m) {
        int min_val = 10;
        if (i + m <= score.size()) {
            for (int j = i; j < i + m; j++) {
                if (score[j] < min_val) {
                    min_val = score[j];
                };
            };
            answer += min_val * m;
        }
        
    }
    
    return answer;
}