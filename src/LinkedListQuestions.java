import java.util.*;

public class LinkedListQuestions {
    static void run_demo() {
        // Set up basic linked list
        ListNode head = new ListNode(1);
        ListNode cycleNode = null;

        ListNode cur = head;
        for(int i = 2; i <= 10; i++){
            cur.next = new ListNode(i);
            if(i == 5)
                cycleNode = cur;
            cur = cur.next;
        }

        cur = cycleNode;

        printList(head);

        System.out.println("Is cycle? " + hasCycle(head));

        // ListNode newhead = reverseList(head);
        // printList(newhead);
    }

    static ListNode reverseList(ListNode head) {
        // Every iteration scout and c starts same place
        ListNode prev = null;
        ListNode c = head;
        ListNode scout = c; // scout should always start the iteration at the same place as current

        while(c != null){
            scout = c.next;
            c.next = prev;
            prev = c;
            c = scout;
        }

        return prev;
    }

    // Print it
    static void printList(ListNode head){
        ListNode cur = head;
        while(cur != null){
            System.out.print(cur.val + " ");
            cur = cur.next;
        }
        System.out.println();
    }

    // Check for cycle
    static boolean hasCycle(ListNode head) {
        if (head == null) return false;

        ListNode slow = head;
        ListNode fast = head;

        StringBuilder sbslow = new StringBuilder();
        StringBuilder sbfast = new StringBuilder();

        while (fast.next != null || fast.next.next != null) {     // While haven't found a non-cycle list
            sbslow.append(slow.val + " ");
            if(fast != null)
                sbfast.append(fast.val + " ");

            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow){
                System.out.println(sbslow.toString());
                System.out.println(sbfast.toString());
                return true;
            }
        }

        System.out.println(sbslow.toString());
        System.out.println(sbfast.toString());
        return false;
    }

    static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // l = length of the longer list BEFORE intersection point and y = length of either list AFTER insection point
        // Likewise s = length of shorter list BEFORE instersection point. x = the required length to make s as long as l
        //      l+y = x+s+y because they intersect at some point. Therefore x = l-s
        //      (l+y) - (s+y) = x
        //      (l+y) = shorter list's length and (s+y) = longer list's length

        if(headA == null || headB == null) return null;

        int lenA = 0;
        int lenB = 0;
        int offset = 0;
        ListNode c_longer, c_shorter;

        // Get length of both list
        ListNode c = headA;
        while(c!= null){
            lenA++;
            c = c.next;
        }

        c = headB;
        while(c!= null){
            lenB++;
            c = c.next;
        }

        // Figure out which list is longer and set the correct pointers on them
        offset = Math.abs(lenA-lenB);

        if(lenA > lenB){
            c_longer = headA;
            c_shorter = headB;
        } else {
            c_longer = headB;
            c_shorter = headA;
        }

        // Walk the the longer list up by the offset so it can be equal same distance from the end as the shorter list
        for(int i = 0; i < offset; i++)
            c_longer = c_longer.next;

        // Check for intersection now that they're both starting from the same distance from the end
        while(c_longer != null){
            if(c_longer == c_shorter)
                return c_longer;
            c_longer = c_longer.next;
            c_shorter = c_shorter.next;
        }

        return null;
    }
}


