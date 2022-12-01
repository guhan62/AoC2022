#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <sstream>

using namespace std;

int main () {
    ifstream elves_calories_list ("Day1_input");
    string calorie_feed;
    int calorie_count, tmp;
    priority_queue<int> Q;
    if( elves_calories_list.is_open() ) {
        while( getline(elves_calories_list, calorie_feed) ) {
            cout<<calorie_feed<<" ";
            if( calorie_feed == "" ) {
                Q.push(calorie_count);
                calorie_count = 0;
                continue;
            }
            stringstream ss(calorie_feed);
            ss >> tmp;
            calorie_count += tmp;
        }
    }
    cout<<Q.top()<<" ";
    return 0;
}