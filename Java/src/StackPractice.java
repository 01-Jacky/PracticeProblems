import java.math.*;
import java.util.*;

public class StackPractice {
    static void run_demo(){
        Stack<Integer> stack = new Stack<Integer>();
        for(int i = 1 ; i <= 10; i++){
            stack.push(i);
        }

        while(!stack.empty())
            System.out.print(stack.pop() + " ");
    }
}
