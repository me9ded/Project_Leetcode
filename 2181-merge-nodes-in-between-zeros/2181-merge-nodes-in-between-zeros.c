/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeNodes(struct ListNode* head) {
    head=head->next;
    if(!head){
        return NULL;
    }
    struct ListNode* temp=head;
    int res=0;
    while(temp->val!=0){
        res+=temp->val;
        temp=temp->next;
    }
    head->val=res;
    head->next=mergeNodes(temp);
    return head;
}