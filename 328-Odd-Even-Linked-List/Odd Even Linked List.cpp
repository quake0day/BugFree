/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (head==NULL || head->next==NULL) return head;

        ListNode* pOdd = head;
        ListNode* evenHead = head->next;
        ListNode* pEven = evenHead;

        while (pEven->next) {
            pOdd->next = pOdd->next->next;
            pOdd = pOdd->next;

            if (pOdd->next) {
                pEven->next = pOdd->next;
                pEven = pEven->next;
            } else {
                pEven->next = NULL;
            }
        }

        pOdd->next = evenHead;
        pEven->next = NULL;

        return head;
    }
};