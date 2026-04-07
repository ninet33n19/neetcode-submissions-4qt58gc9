class Solution {
  public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charMapS;
        unordered_map<char, int> charMapT;

        for (char c : s) { charMapS[c]++; }
        for (char c : t) { charMapT[c]++; }

        if (charMapS == charMapT) { return true; }

        return false;
    }
};