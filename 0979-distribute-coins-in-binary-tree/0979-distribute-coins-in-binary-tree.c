/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int dfs(struct TreeNode* root,struct TreeNode* parent){
    if(!root){
        return 0;
    }
    int moves=dfs(root->left,root)+ dfs(root->right,root);
    int x=root->val-1;
    if(parent){
        parent->val+=x;
    }
    moves+=abs(x);
    return moves;
 }
int distributeCoins(struct TreeNode* root) {
    return dfs(root,NULL);
    
}