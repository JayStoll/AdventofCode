#include <iostream>
#include <fstream>
#include <string>
#include <regex>

int main() {
    int low;
    int high;
    int validPass = 0;

    std::string line;
    std::string letter;
    std::string password;

    std::regex wr("[^\\s.,:;!?-]+");

    std::ifstream f("input.txt");
    while (std::getline(f, line)) {
        std::string toParse[10];

        auto s = std::sregex_iterator(line.begin(), line.end(), wr);
        auto end = std::sregex_iterator();
        int j = 0;
        for (std::sregex_iterator i = s; i != end; i++) {
            toParse[j] = (*i).str();
            j++;
        }

        low = std::stoi(toParse[0]);
        high = std::stoi(toParse[1]);
        letter = toParse[2];
        password = toParse[3];

        int count = 0;
        for (int i = 0; i < password.length(); i++) {
            if (password[i] == letter[0]) count++;
        }
        if (count >= low && count <= high) validPass++;
    }
    f.close();


    std::cout << validPass;

    std::cin.get();
    return 0;
}