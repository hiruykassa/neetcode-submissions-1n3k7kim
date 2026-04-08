class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    nums = [1,1,1,1,2,2,3,3,3]
    topKFrequent(nums, k) {
        let hash = new Map();

        for(let i = 0; i < nums.length; i++){
            if(!hash.has(nums[i]))hash.set(nums[i], 1);
            else hash.set(nums[i], hash.get(nums[i]) + 1);
        }
        let answer = []; //k length
        let keys = [...hash.keys()];
        let maxIndex = -1;
        // [1,2,2,3,3,3]
        for(let j = 0; j < k; j++){
            for(let i = 0; i < keys.length; i++){
                if(maxIndex == -1 && !answer.includes(keys[i])) maxIndex = i;
                if(hash.get(keys[i]) > hash.get(keys[maxIndex]) && !answer.includes(keys[i])) maxIndex = i;
            }
            answer.push(keys[maxIndex]);
            maxIndex = -1;
        }
        return answer;
    }
}
