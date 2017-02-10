import java.util.*;

public class LinkedListPractice {
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

        printList(head);
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
}


