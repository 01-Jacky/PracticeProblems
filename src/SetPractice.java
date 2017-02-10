import java.util.*;

public class SetPractice {
    static void run_demo() {
        Set<Integer> set = new HashSet<>();

        set.add(5);
        set.add(1);
        set.add(9);
        set.add(3);

        for(Integer i : set)
            System.out.print(i + " ");
    }
}