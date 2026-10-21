#include <vector>
#include <algorithm>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        // Sort the vector in-place (O(1) extra memory)
        std::sort(nums.begin(), nums.end());
        
        // Check adjacent elements
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        
        return false;
    }
};