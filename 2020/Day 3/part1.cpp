#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    int j = 0;
    int k = 0;
    int tree = 0;
    
    std::vector<std::string> a;
    std::string line;

    std::fstream f("input.txt");
    while (std::getline(f, line)) {
        a.push_back(line);
    }

    while (k < a.size()) {
        tree += a[k][j % a[0].size()] == '#';
        j += 3;
        k += 1; 
    }

    std::cout << tree;

    return 0;
}