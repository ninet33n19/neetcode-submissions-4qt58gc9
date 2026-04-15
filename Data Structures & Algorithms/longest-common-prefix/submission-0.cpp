class Solution {
  public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        if (strs.size() == 1) return strs[0];

        string result = "";

        for (int i = 0; i < strs[0].size(); ++i) {
            char ch = strs[0][i];

            for (int j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].size() || strs[j][i] != ch) { return result; }
            }
            result += ch;
        }

        return result;
    }
};