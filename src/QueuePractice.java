import java.util.*;

public class QueuePractice {
    static void run_demo() {
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 1 ; i <= 10; i++){
            queue.add(i);
        }

        while(queue.size() != 0)
            System.out.print(queue.remove() + " ");
    }
}
