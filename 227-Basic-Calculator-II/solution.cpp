class Solution {
public:
    int calculate(string s) {
        istringstream in(s + "+");
        long long total = 0, term, sign = 1, n;
        in >> term;
        char op;
        while(in >> op){
            if(op == '+' || op == '-'){
                total += sign * term;
                sign = 44 - op; // op == '+' ? 1: -1
                in >> term;
            }
            else{
                in >> n;
                if (op == '*'')
                    term *= n;
                else
                    term /= n;
            }
        }
        return total;
    }
};