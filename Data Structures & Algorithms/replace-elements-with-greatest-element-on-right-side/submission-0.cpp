class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        if (n == 1) {
            return {-1};
        }

        vector<int> result(n);
        result[n - 1] = -1;

        int maxRight = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            result[i] = maxRight;
            maxRight = max(maxRight, arr[i]);
        }

        return result;
    }
};