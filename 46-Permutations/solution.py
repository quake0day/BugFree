class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret = {{}};
        for(int n : nums){
            vector<vector<int>> temp;
            for(auto x : ret){
                for(int i = 0; i <= x.size(); i++){
                    vector<int> t = x;
                    t.insert(t.begin()+i, n);
                    temp.push_back(t);
                }
            }
            ret.swap(temp);
        }
        return ret;
    }
    
};