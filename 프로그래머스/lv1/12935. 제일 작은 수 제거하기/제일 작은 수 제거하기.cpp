#include <string>
#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int n = 1000000;
    for (int i : arr) {
        n = min(n, i);
    };
    
    for (int i = 0; i < arr.size(); i++) {
        if (n != arr[i]) answer.push_back(arr[i]);
    };
    if (answer.empty()) answer.push_back(-1);
    
    return answer;
}