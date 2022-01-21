#include <iostream>
#include <string>
#include <stack>
#include <vector>
using namespace std;

int main() {
    // Sort Two Numbers

    int a, b;
    cin >> a >> b;
    if (a > b) {
        cout << b << " " << a;
    } else {
        cout << a << " " << b;
    }


    // Magic Trick
    /*
    string s;
    cin >> s;
    stack<string> storage;
    for (int i = 0; i < s.size(); i++) {

    }

    */

    // Odd Echo
    /*
    int a;
    // cout << "Enter number: ";
    cin >> a;
    vector<string> storage;
    for (int i = 0; i < a; i++) {
        // cout << "Enter word: ";
        string word;
        cin >> word;
        storage.push_back(word);
    }
    for (int i = 0; i < a; i++) {
        if (i % 2 == 0) {
            cout << storage[i] << endl;
        }
    }
     */

    // Provinces and Gold
    /*
    int gold, silver, copper;
    cin >> gold >> silver >> copper;
    int totalBuyingPower = gold * 3 + silver * 2 + copper;
    if (totalBuyingPower >= 8) {
        cout << "Province or Gold";
    } else if (totalBuyingPower >= 6) {
        cout << "Duchy or Gold";
    } else if (totalBuyingPower >= 5) {
        cout << "Duchy or Silver";
    } else if (totalBuyingPower >= 3) {
        cout << "Estate or Silver";
    } else if (totalBuyingPower >= 2) {
        cout << "Estate or Copper";
    } else { cout << "Copper"; }
    */

    // Autori
    /*
    string input;
    string output;
    cin >> input;
    output += input[0];
    for (int i = 0; i < input.length(); i++) {
        if (input[i] == '-') {
            output = output + input[i + 1];
        }
    }
    cout << output;
    */

    // Triple Texting



    // Alphabet Spam
    /*
    string titleChars;
    char output;
    cin >> titleChars;
    output += titleChars[0];
    double whitespace = 0;
    double lowercase = 0;
    double uppercase = 0;
    double symbols = 0;
    for (int i = 0; i < titleChars.length(); i++) {
        if (titleChars[i] == '_') {
            whitespace++;
        }
        if (titleChars[i] > 96 && titleChars[i] < 123) {
            lowercase++;
        }
        if (titleChars[i] > 64 && titleChars[i] < 91) {
            uppercase++;
        }
        if ((titleChars[i] >= 33 && titleChars[i] <= 64) || (titleChars[i] >= 123 && titleChars[i] <= 126) ||
        (titleChars[i] >= 90 && titleChars[i] <= 96 && titleChars[1] != 95) || (titleChars[i] >= 161 && titleChars[i] <= 255)) {
            symbols++;
        }
    }
    // cout << whitespace;
    // cout << lowercase;
    // cout << uppercase;
    // cout << symbols;
    cout << (whitespace / titleChars.length()) << endl;
    cout << (lowercase / titleChars.length()) << endl;
    cout << (uppercase / titleChars.length()) << endl;
    cout << (symbols / titleChars.length()) << endl;
    */

    // Apaxiaaaaaaaaaaaaaans!
    /*
    string input, compact;
    cin >> input;
    compact += input[0];
    for (int i = 0; i < input.length(); i++) {
        if (input[i] != compact[compact.length() - 1]) {
            compact += input[i];
        }
    }
    cout << compact;
     */


}
