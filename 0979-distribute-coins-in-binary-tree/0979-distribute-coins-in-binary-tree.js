/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var distributeCoins = function(root,parent) {
    if(!root){
        return 0;
    }
    let moves=distributeCoins(root.left,root)+distributeCoins(root.right,root);
    let x=root.val-1;
    if(parent){
        parent.val+=x;
    }
    moves+=Math.abs(x);
    return moves
};