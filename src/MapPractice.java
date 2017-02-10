import java.util.*;

public class MapPractice {
    static void run_demo(){
        Hashtable<String, Integer> table = new Hashtable<>();                   // Synchronized, thread safe
        HashMap<String, Integer> map = new HashMap<>();                         // Un-synchronized, unsorted

        TreeMap<String, Integer> tree_map_natural_order = new TreeMap<>();      // O(logn) instead of O(1) but retains order

        Map<String, Integer> tree_map_lambda = new TreeMap<>( (String o1, String o2) -> o2.compareTo(o1) );
        TreeMap<String, Integer> tree_map_comparator = new TreeMap<>(
                new Comparator<String>() {
                    @Override
                    public int compare(String o1, String o2) {
                        return o2.compareTo(o1);
                    }
                }
        );

//        System.out.println("Testing map...");
//        map.put("Dan",2);
//        map.put("Anne",10);
//        map.put("Chris",4);
//
//        boolean hasKey = map.containsKey("Dan");
//        int value = map.get("Dan");

        System.out.println("Testing TreeMap sorting...");

        tree_map_lambda.put("Dan",2);
        tree_map_lambda.put("Anne",10);
        tree_map_lambda.put("Chris",4);
        // tree_map_lambda.put

        for(Map.Entry<String,Integer> entry : tree_map_lambda.entrySet()) {
            System.out.println(entry.getKey() + " => " + entry.getValue());
        }
    }
}
