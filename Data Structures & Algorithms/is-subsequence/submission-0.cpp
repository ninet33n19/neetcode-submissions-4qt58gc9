class Solution {
public:
    bool isSubsequence(string s, string t) {
        int j = 0;
        for(int i = 0; i < s.length(); i++) {
            bool found = false;
            while(j < t.length()) {
                if(s[i] == t[j++]) {
                    found = true;
                    break;
                }
            }
            if (!found) return false;
        }

        return true;
    }
};