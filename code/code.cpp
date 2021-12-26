#include <fstream>
#include <iostream>
#include <string>

using namespace std;



int main (){
    string line;
    ifstream inFile;
    inFile.open("/home/steven/projects/cipher_fun/vigenere_cracker/source_text/cipher_text.txt");

    if (inFile.is_open())
    {
        while (char = get(inFile))
        {
            char = get(inFile);
            cout << char << '\n';
        }
        inFile.close();
    }

    else cout << "Unable to open file";

    return 0;
}