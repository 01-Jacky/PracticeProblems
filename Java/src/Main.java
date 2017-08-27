// Add these imports
import java.lang.reflect.Array;
import java.math.*;
import java.util.*;
import java.util.Map;

public class Main {
    static class Trade{
        public int day;
        public String trader;
        public boolean buyOrder;
        public int price;
        public int quantity;

        Trade(){
        }

        Trade(int day, String trader, boolean buy, int price, int quantity){
            this.day = day;
            this.trader = trader;
            this.buyOrder = buy;
            this.price = price;
            this.quantity = quantity;
        }
    }

    public static void main(String[] args) {
        // System.out.println("Program begin...");


        HashMap<Integer,ArrayList<String>> map = new HashMap<>();

        ArrayList<String> list = map.putIfAbsent(0,new ArrayList<String>());
        if(list != null){
            list.add("a");
            map.put(0,list);
        }

        list = map.putIfAbsent(0,new ArrayList<String>());
        if(list != null){
            list.add("b");
            map.put(0,list);
        }

        System.out.println(map.get(0).toString());

        ///////////////// Strings, Arrays, and List /////////////////
        ///// Strings
        // StringQuestions.run_demo();

        ///// Arrays
        // ArrayQuestions.run_demo();

        ///// 2D Array (Matrix)
        // MatrixQuestions.run_demo();


        ///// ArrayList

        ///////////////// Data Structures /////////////////

        // Stack
        // StackPractice.run_demo();

        // Queue
        // QueuePractice.run_demo();

        // PQ
        // PriorityQueuePractice.run_demo();

        // Set
        // SetPractice.run_demo();

        // Map
        //MapPractice.run_demo();

        ///////////////// Data Types /////////////////
        // LinkedList
        // LinkedListPractice.run_demo();

        ///// Trees
        // TreePractice.run_demo();
        // TreeQuestions.run_demo();


        // Heap

        ///////////////// Math  /////////////////
        // MathQuestions.run_demo();


    }

}
