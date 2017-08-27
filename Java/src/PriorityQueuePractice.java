import java.util.*;

public class PriorityQueuePractice {
    static void run_demo() {
        // Natural Order
        PriorityQueue<Integer> queue_naturalOrder = new PriorityQueue<>();   // natural ordering
        queue_naturalOrder.add(5);
        queue_naturalOrder.add(3);
        queue_naturalOrder.add(1);
        queue_naturalOrder.add(9);

        while (queue_naturalOrder.size() != 0)
            System.out.print(queue_naturalOrder.remove() + " ");
        System.out.println();

        // Iterable natural order
        ArrayList<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(3);
        list.add(1);
        list.add(9);

        PriorityQueue<Integer> queue_iterable = new PriorityQueue<>(list);

        while (queue_iterable.size() != 0)
            System.out.print(queue_iterable.remove() + " ");
        System.out.println();

        // Supplying comparator
        PriorityQueue<Integer> queue_constructor = new PriorityQueue<Integer>(10, (Integer o1, Integer o2) -> o1.compareTo(o2) );
        queue_constructor.add(5);
        queue_constructor.add(3);
        queue_constructor.add(1);
        queue_constructor.add(9);

        while (queue_constructor.size() != 0)
            System.out.print(queue_constructor.remove() + " ");
        System.out.println();

    }
}
