class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;
        unordered_map<char, int> mp;

        for(char c : jewels){
            mp[c]++;
        }

        for(int i = 0; i < stones.size(); i++){
            if(mp.find(stones[i]) != mp.end()){
                res++;
            }
        }

        return res;
    }
};