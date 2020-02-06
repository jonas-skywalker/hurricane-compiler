#include <iostream>
#include <fstream> 
#include <algorithm>
#include <string.h>

using namespace std;

int main() {
    string data;

    ifstream datei;
    datei.open("material/hallo.txt");
    datei >> data;

    data.erase(remove(data.begin(), data.end(), ' '), data.end());

    cout << data << endl;
    cout << "hallo" << endl;
    return 0;
}