/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(!head)
            return NULL;
        RandomListNode* p;
        RandomListNode* q;
        
        // First interleave list
        p = head;
        while (p){
            q = new RandomListNode(p->label);
            q->next = p->next;
            p->next = q;
            p = q->next;
        }
        p = head;
        while(p){
            if(p->random){
                p->next->random = p->random->next;
            }
            p = p->next->next;
        }
        RandomListNode* newHead = head->next;
        p = head;
        q = newHead;
        while(p){
            p->next = q->next;
            q->next = (p->next ? p->next->next : NULL);
            q = q->next;
            p = p->next;
        }
        return newHead;
        
    }
};