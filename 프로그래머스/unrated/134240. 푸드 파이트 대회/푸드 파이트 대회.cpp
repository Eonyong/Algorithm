#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<int> food) {
    string answer = "0";
    string left = "";
    string right = "";
    
    for(int i = 1; i < food.size();i++) {
        string alpha = to_string(i);
        for(int j = 0; j < food[i] / 2;j++) {
            right.insert(0, alpha);
            left.insert(left.length(), alpha);      
        }
    }
    return left + answer + right;
}