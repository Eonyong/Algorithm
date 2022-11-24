#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int hashard = 0;
    int y = x;
    while(y) {
        hashard += y % 10;
        y = int(y / 10);
    };
    return !(x % hashard);
}