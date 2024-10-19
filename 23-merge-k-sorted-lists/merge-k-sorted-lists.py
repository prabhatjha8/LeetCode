# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        ans = []
        priorityQueue = []
        heapq.heapify(priorityQueue)

        def initiate(lists):
            cnt = 0
            for i in range(k):
                if lists[i] != None:
                    heapq.heappush(priorityQueue, (lists[i].val, i))
                    lists[i] = lists[i].next
                    cnt +=1
            return (cnt != 0)

        while True:
            if not priorityQueue:
                decision = initiate(lists)
                if not decision:
                    break

            val, ind = heapq.heappop(priorityQueue)
            ans.append(val)

            if lists[ind] != None:
                heapq.heappush(priorityQueue, (lists[ind].val, ind))
                lists[ind] = lists[ind].next

        if not ans:
            return None

        toReturn = ListNode(ans[0])
        toReturnCopy = toReturn
        for i in range(1, len(ans)):
            toReturnCopy.next = ListNode(ans[i])
            toReturnCopy = toReturnCopy.next
        
        return toReturn





        



        