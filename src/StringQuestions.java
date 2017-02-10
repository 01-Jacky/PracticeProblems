import java.util.*;


public class StringQuestions {
    public static void run_demo() {



        //
        // permutation("abcde");


        count1bits(2314);


        // System.out.println(StringQuestions.isPalindrome("aba"));

        ///////////////// Testing String to Int atoi
        // String s = "  +1002";
        // System.out.println(myAtoi(s));


        ///////////////// Testing replacepattern
        // String s = "zzabczzabczzabcabczz";
        // System.out.println(replacePattern(s,"abc","1234"));

        ///////////////// Testing replacechar
        // String s = "abcabca abcabc zz";
        // System.out.println(replaceChar(s,'c',"123"));


        ///////////////// Testing roman to int
        // String s = "XXI";
        // System.out.println(s + " = " + romanToInt(s));
        // s = "XXIV";
        // System.out.println(s + " = " + romanToInt(s));
        // s = "XXVII";
        // System.out.println(s + " = " + romanToInt(s));

        ///////////////// Testing string rotation
        // System.out.println(isRotation("laepp","apple"));    // false
        // System.out.println(isRotation("leapp","apple"));    // true


        ///////////////// Testing countParenthesis()
        // String s = "(())";
        // System.out.println("Input: " + s + "\nOutput: " + countParenthesis(s));
        // s = "(()";
        // System.out.println("Input: " + s + "\nOutput: " + countParenthesis(s));

        ///////////////// Testing isValidParenthesis()
        // String s = "(())";
        // System.out.println("Input: " + s + "\nOutput: " + isValidParenthesis(s));
        // s = "(()";
        // System.out.println("Input: " + s + "\nOutput: " + isValidParenthesis(s));
        // s = ")((";
        // System.out.println("Input: " + s + "\nOutput: " + isValidParenthesis(s));
        // s = "(1+2*(3-2))/(2-5)";
        // System.out.println("Input: " + s + "\nOutput: " + isValidParenthesis(s));
        // s = "(1+2*)(3-2))/(2-5)";
        // System.out.println("Input: " + s + "\nOutput: " + isValidParenthesis(s));


        ///////////////// Testing printing excel cell names
        // System.out.println(cellName(3,3));
    }

    // Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    // https://leetcode.com/problems/valid-palindrome/Valid Palindrome
    public static boolean isPalindrome(String s) {
        if (s.isEmpty()) {
            return true;
        }

        // Use two indexes heading towards each other and skip the indexes that are not alpanumeric
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            while (!Character.isLetterOrDigit(s.charAt(i)) && i < s.length() - 1) {
                i++;
            }
            while (!Character.isLetterOrDigit(s.charAt(j)) && j >= i) {
                j--;
            }

            if (i <= j && Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
        }
        return true;
    }

    // Inputs is a string consisting of only ( or ). Return the # of matching pairs or -1 if unbalanced.
    static int countParenthesis(String str) {
        // e.g. String str = "(())";
        int pairs = 0;

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                stack.push(str.charAt(i));
            } else {
                if (stack.empty()) {
                    System.out.println(-1);
                } else {
                    stack.pop();
                    pairs++;
                }
            }
        }

        return stack.empty() ? pairs : -1;
    }

    // Determine if a string containning only ( and ) is balanced
    static boolean isValidParenthesis(String str) {
        int counter = 0;

        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == '('){
                counter++;
            } else if(str.charAt(i) == ')'){
                if(counter > 0){
                    counter--;
                } else {
                    return false;
                }
            }
        }

        return counter == 0 ? true : false;
    }

    // Check if a string is a rotation of another, e.g. pleap is a rotation of apple
    static boolean isRotation(String s, String original) {
        if (s.length() != original.length())
            return false;
        String temp = s.concat(s);
        return (temp.indexOf(original) != -1) ? true : false;
    }


    // Get microsoft cell name
    static String cellName(int col, int row) {
        String s = Character.toString((char) (64 + col)) + Integer.toString(row);
        return s;
    }

    // Get MS Excel column number
    static int colNum(String s){
        // Think of each digit as base 26. Second digit place is 26*(whatever that num is).
        // int sum = 0;
        // for(int i = 0; i<s.length(); i++){
        //     sum *= 26;
        //     sum += s.charAt(i)-'A'+1;
        // }
        // return sum;

        // Think regular numbers. 23 = 2*10^1 + 3*10^0. With letters, it's base 26. Therefore AB = 1*26^1 + 2*26^0
        int sum = 0;
        int power = 0;
        for(int i = s.length()-1; i >= 0; i--,power++){
            int charNumber = s.charAt(i)-'A'+1;
            sum += charNumber*Math.pow(26,power);
        }
        return sum;
    }

    // count int to string
    static int count1bits(int n) {
        // String s = Integer.toBinaryString(n);
        // int sum = 0;
        // for(char c : s.toCharArray()){
        //     if(c == '1')
        //         sum++;
        // }
        // return sum;

        // Alternative bit shifting bullshit
        // Take this binary number 10011. If we want to check and count its 1st bit, we can AND it with 00001.
        System.out.println(Integer.toBinaryString(n));
        int ones = 0;
        while(n!=0) {
            ones = ones + (n & 1);
            n = n>>>1;
            System.out.println(Integer.toBinaryString(n));
        }
        return ones;
    }

    // Convert roman number to int
    // https://leetcode.com/problems/roman-to-integer/
    static int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        if (s.length() == 1) {
            return map.get(s.charAt(0));
        } else {
            int total = 0;

            for (int i = 0; i < s.length(); i++) {
                int first = map.get(s.charAt(i));
                int second = (i + 1 < s.length()) ? map.get(s.charAt(i + 1)) : 0;

                if (first < second) {       // subtract
                    total = total - first;
                } else
                    total = total + first;
            }

            return total;
        }
    }

    // Replace a char in a string with another string.
    static String replaceChar(String original, char c_replace, String replace){
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < original.length(); i++){
            if(original.charAt(i) == c_replace){
                sb.append(replace);
            } else {
                sb.append(original.charAt(i));
            }
        }

        return sb.toString();
    }

    static String replacePattern(String original, String pattern, String replace){
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < original.length(); i++){
            // if we find a character that start to match the pattern, check for the pattern
            if(original.charAt(i) == pattern.charAt(0) && original.substring(i,i+pattern.length()).equals(pattern)){
                sb.append(replace);
                i = i + replace.length()-1;
            } else {
                sb.append(original.charAt(i));
            }
        }

        return sb.toString();
    }

    //Find pword
    public static void permutation(String str) {
        permutation_helper("", str);
    }

    private static void permutation_helper(String prefix, String str) {
        int n = str.length();

        if (n == 0)
            System.out.println(prefix);
        else {
            for (int i = 0; i < n; i++)
                permutation_helper(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
        }
    }
    // String to Int atoi
    // https://leetcode.com/problems/string-to-integer-atoi/
    static int myAtoi(String str) {
        StringBuilder sb = new StringBuilder();

        int i = 0;
        int sign = 1;

        // Check empty string
        if(str.length() == 0) return 0;

        // Trim leading white space
        String s_trimmed = str.trim();

        // Get the sign if any
        // if (s.charAt(i) == '-'){
        //     sign = -1;
        // }
        if (s_trimmed.charAt(i) == '-' || s_trimmed.charAt(i) == '+'){
            i++;
        }

        i = 0;

        // Convert number to int
        while(i < s_trimmed.length()) {
            sb.append(s_trimmed.charAt(i));
            i++;
        }

        System.out.println(sb);
        return Integer.parseInt(sb.toString());
    }
}
