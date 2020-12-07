#include <iostream>
#include <fstream>

int main() {
    int x = 0;
    int y = 1;
    bool kill = false; // lazy way to leave loop
    int a[200];


    // Deal with input file - populate array
    std::ifstream f("input.txt");
    if (f.is_open()) {
        for (int i = 0; i < 200; i++) {
            f >> a[i];
        }
    }
    f.close();

    // find numbers
    for (int i = 0; i < 200; i++) {
        for (int j = 0; j < (199 - j); j++) {
            if (a[x] + a[y] == 2020) {
                kill = true;
            } else {
                y++;
            }
        }
        if (kill) break;
        x++;
        y = x+1;
    }

    //std::cout << a[x] << " " << a[y] << std::endl; // just to make sure

    std::cout << a[x] * a[y];

    std::cin.get();
    return 0;
}