class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        /*

        for i in nums:

            check if i is in hmap
            if it is then, return false

            save i to hmap

        return true

        */

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