/**
 * Created by hklee on 2/14/2017.
 */
public class MathQuestions {

    public static void run_demo() {
        System.out.println(countPrimes(15));
    }

    static int countPrimes(int n) {
        // Brute force
        // int count = 0;
        // for(int i = 2; i<n ;i++) {
        //     if(isPrime(i))
        //         count++;
        // }
        // return count;

        boolean[] notPrime = new boolean[n];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrime[i] == false) {
                count++;
                for (int j = 2; i*j < n; j++) {
                    notPrime[i*j] = true;
                }
            }
        }

        return count;
    }

    static boolean isPrime(int n){
        for(int i = 2; i<n-1; i++){
            if(n % i == 0)
                return false;
        }
        return true;
    }
}
