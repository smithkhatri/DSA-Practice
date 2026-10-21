class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        #include <iostream>
        #include <unordered_set>
        #include <string>

        std::unordered_set<int> hset;


        for (int i=0; i<nums.size(); i++){
            if (hset.count(nums[i])){
                return true;
            }

            hset.insert(nums[i]);
        }

        return false;


    }
};