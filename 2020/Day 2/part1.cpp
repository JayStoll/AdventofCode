#include <iostream>
#include <fstream>
#include <string>

int main() {
    int low;
    int high;

    int validCount = 0;
    int validPass = 0;

    std::string line;
    std::string toParse;
    char letter;
    std::string password;




    std::ifstream f("input.txt");
    while (f.eof()) {
        std::cout << validCount << std::endl;
        validCount++; 
    }
    f.close();


    // std::ifstream f("input.txt");
    // while(!f.eof(), i < 1000) {
    //     std::getline(f, a[i]);
    //     i++;
    // }
    // f.close();

    // for (int i = 0; i < sizeof(a)/sizeof(*a); i++) {
    //     line = a[i];
    //     std::string p;
    //     p.push_back(line[0]);
    //     low = std::stoi(p);
    //     p = ""; // flush variable
    //     p.push_back(line[2]);
    //     high = std::stoi(p);
    //     letter = line[4];


    //     for (int j = 0; j < line.length(); j++) {
    //         if (j >=7) password += line[j];
    //     }

    //     for (int k = 0; k < password.length(); k++) {
    //         if (password[k] == letter) validCount++;
    //     }
    //     if (validCount >= low && validCount <= high) validPass++;
    //     else std::cout << "invalid\n";
        
    //     validCount = 0;

    // }


    std::cin.get();
    return 0;
}