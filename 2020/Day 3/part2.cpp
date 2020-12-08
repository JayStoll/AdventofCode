#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int Count(int x, int y, std::vector<std::string> a) {
    int j = 0;
    int k = 0;
    int tree = 0;

    while (k < a.size()) {
        tree += a[k][j % a[0].size()] == '#';
        j += x;
        k += y; 
    }
    return tree;
}

int main() {
    std::vector<std::string> a;
    std::string line;

    std::fstream f("input.txt");
    while (std::getline(f, line)) {
        a.push_back(line);
    }

    // just trying to std::cout << Count(1, 1, a) * Count(3, 1, a) ... gave me errors so just did this as a quick fix
    unsigned int t = Count(1, 1, a) * Count(3, 1, a) * Count(5, 1, a) * Count(7, 1, a) * Count(1, 2, a);
    std::cout << t;

    return 0;
}