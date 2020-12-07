#include <iostream>
#include <fstream>

int main() {
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

    for (int i : a) {
        for (int j : a) {
            for (int k : a) {
                if (i + j + k == 2020) {
                    std::cout << i*j*k << std::endl;
                    kill = true;
                    break;
                }
            }
            if (kill) {
                break;
            }
        }
        if (kill) {
            break;
        }
    }

    std::cin.get();
    return 0;
}