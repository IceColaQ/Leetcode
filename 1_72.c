#include <string.h>
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        int dp[m+1][n+1];
        
        int i,j;

        for (i=0;i<m+1;++i){
            dp[i][0] = i;
        }
        for (i=0;i<n+1;++i){
            dp[0][i] = i;
        }

        for (i=1;i<m+1;i++){
            for (j=1;j<n+1;j++){
                if (word1[i-1]==word2[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }
                else{
                    dp[i][j] = min(dp[i-1][j-1]+1,min(dp[i][j-1]+1,dp[i-1][j]+1));
                }
            }
        }
        return dp[m][n];
    }
};
// 这是Leetcode的第一题...
// 为什么写这个题呢 是因为生物信息学的作业其中一问是和这个非常类似的
// 计算 ‘ACTG’ 和 ‘GGTC’ 的edit distance。
// 在同学的指导下，在leetcode上找到了对应的题目。

// 这是一个Hard题目 本来是一脸懵逼的说实话 而且好久没有正经用c++写代码了
// 作业大部分是C，然后机器学习基本上都用的python。
// 感觉还是很棒的，希望自己能坚持用c++刷题。

// 从一头雾水到做出来 还是很有成就感的！ 很开心！