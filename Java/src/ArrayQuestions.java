import java.util.*;

/**
 * Created by hklee on 1/15/2017.
 */
public class ArrayQuestions {

    public static void run_demo(){


        ///////////////////// Testing merge sorted array in place
        // int[] nums1 = new int[]{0};
        // int[] nums2 = new int[]{1};
        // mergeSortedArrays_inplace(nums1,1,nums2,1);

        ///////////////////// Testing maxProfit
        // int[] prices = new int[]{1,2};
        // System.out.println("Max profit: " + maxProfit(prices));
        //
        // prices = new int[]{7, 6, 4, 3, 1};
        // System.out.println("Max profit: " + maxProfit(prices));


        ///////////////////// Testing twoSum
        // int[] nums = new int[]{3,2,4};
        // int target = 6;
        // int[] ans = twoSum(nums, target);
        // System.out.println(ans[0] + " " + ans[1]);

            ///////////////////// Testing minDifference
        // int[] arr1 = new int[]{1,2,11,15};
        // int[] arr2 = new int[]{4,12,19,23,127,235};
        // int [] answer = minDifference(arr1,arr2);
        // System.out.println("Min is: " + answer[0] + " which is created by the pair " + answer[1] + " and " + answer[2]);
        //
        // arr1 = new int[]{1,3,15,11,2};
        // arr2 = new int[]{23,127,235,19,8};
        // answer = minDifference(arr1,arr2);
        // System.out.println("Min is: " + answer[0] + " which is created by the pair " + answer[1] + " and " + answer[2]);


        // System.out.println(containsDuplicate(new int[]{1,2,3,4,5,7,6,5}));

        // int[] arr = mergeSortedList(new int[]{1,3,5,9}, new int[]{2,6,7,8,10});
        // for(int i : arr)
        //     System.out.print(i + " ");

        ///////////////////// Testing mergeSortedList_inplace
        // int[] arr1 = new int[5];
        // arr1[0] = 1;
        // arr1[1] = 3;
        // int[] arr2 = new int[]{2,4,6};
        // mergeSortedList_inplace(arr1,5, arr2,3);
        // for(int i : arr2)
        //     System.out.print(i + " ");



    }

    // Contains Duplicates
    // Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
    // https://leetcode.com/problems/contains-duplicate/
    public static boolean containsDuplicate(int[] nums) {
        // Keep a set of seen nums, uses extra space
        Set<Integer> set_seen = new HashSet<Integer>();
        for(int i : nums){
            if(set_seen.contains(i)){
                return true;
            } else {
                set_seen.add(i);
            }
        }
        return false;

        //// No extra space solution: sort and check adjacent
        //Arrays.sort(nums);
        //for(int i = 1; i< nums.length; i++){
        //    if(nums[i] == nums[i-1])
        //        return true;
        //}
        //return false;
    }

    // Contains Nearby Duplicates
    // Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
    // https://leetcode.com/problems/contains-duplicate-ii/
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        // Use a sliding window; remove values no longer in the window, and then check the current value
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i - k - 1]);
            if(!set.add(nums[i])) return true;
        }
        return false;
    }



    // Check two sums
    // Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    // https://leetcode.com/problems/two-sum/
    static int[] twoSum(int[] nums, int target){
        // Pain point is having to lookup repeatably if the required value is in the array.
        // Use a map that maps the integer to its index. For each number, check the map for the needed number and then get the index.
        int[] result_indexes = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        // Make a map of the integers and its index
        for(int i=0; i<nums.length; i++){               //O(n)
            int numNeeded = target - nums[i];

            if(map.containsKey(numNeeded)){
                result_indexes[0] = i;                          //O(1)
                result_indexes[1] = map.get(numNeeded);
                return result_indexes;
            } else {
                map.put(nums[i],i);                            //O(1)
            }
        }

        return result_indexes;      // Total O(n) runtime, O(n) space

        // // If want to optimize space over time, sort the array and do binary search on the shorter side
        // // Actually we can't do this because the shuffle loses the indexs.... we can only return the pair of numbers
        // int[] result = new int[2];
        //
        // Arrays.sort(nums);          // O(n log n)
        //
        // for(int i=0; i<nums.length; i++){       //O(n)
        //     int dif = target - nums[i];
        //     int indexFound = -1;
        //     if(i+1 < nums.length)
        //         indexFound = Arrays.binarySearch(nums,1,nums.length,dif);     // O(n)
        //
        //     if(indexFound > 0) {
        //         result[0] = nums[i];
        //         result[1] = nums[indexFound];
        //         return result;
        //     }
        // }
        //
        // return result;      // Total O(n log n) time, O(1) space.
    }


    public static int[] mergeSortedArrays(int[] nums1, int m, int[] nums2,int n) {
        int[] arr = new int[nums1.length + nums2.length];
        int c1 = 0;
        int c2 = 0;

        for(int i = 0; i < arr.length; i++){
            if(c1 > nums1.length-1) {    // If nums1 is at the end just fill with c2
                arr[i] = nums2[c2];
                c2++;
            } else if(c2 > nums2.length-1) {    // If nums2 is at the end just fill with c1
                arr[i] = nums1[c1];
                c1++;
            } else {
                if(nums1[c1] <= nums2[c2])
                    arr[i] = nums1[c1++];
                else
                    arr[i] = nums2[c2++];
            }
        }

        return arr;
    }

    static void mergeSortedArrays_inplace(int[] nums1, int m, int[] nums2, int n) {
            // Use a new array and copy over the greater head value in each list
            int[] arr = new int[nums1.length + nums2.length];
            int c1 = 0;
            int c2 = 0;

            for(int i = 0; i < arr.length; i++){
                if(c1 > nums1.length-1) {    // If nums1 is at the end just fill with c2
                    arr[i] = nums2[c2];
                    c2++;
                } else if(c2 > nums2.length-1) {    // If nums2 is at the end just fill with c1
                    arr[i] = nums1[c1];
                    c1++;
                } else {
                    if(nums1[c1] <= nums2[c2])
                        arr[i] = nums1[c1++];
                    else
                        arr[i] = nums2[c2++];
                }
            }

            if(nums1.length < arr.length)
                return;

            for(int i = 0; i < arr.length; i++){
                nums1[i] = arr[i];
            }
        }


    // Remove Duplicates from Sorted Array (in O(1) space);
    // Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory.
    // https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    public int removeDuplicates_sortedArray(int[] nums) {
        // When dups happen, use a count to find the # of offset you need
        int count = 0;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i-1])
                nums[i-count] = nums[i];
            else
                count++;
        }

        return nums.length-count;
    }

    // CTCI 16.6 Find Min diference between 2 array of ints
    // Returns an array where 1st value is the min, and followed by the pair that made the difference
    public static int[] minDifference(int[] arrA, int[] arrB){
        int min = Integer.MAX_VALUE;
        int[] answer = new int[3];

        Arrays.sort(arrA);  // Quicksort O(n log n)
        Arrays.sort(arrB);

        int i = 0;
        int j = 0;
        while(i < arrA.length-1 && j < arrB.length-1){
            // Check min
            int dif = Math.abs(arrA[i]-arrB[j]);
            if( dif < min) {
                min = dif;
                answer[0] = min;
                answer[1] = arrA[i];
                answer[2] = arrB[j];
            }

            // Find next dif pair. If a is smaller than b, then we need to test the next a (because the next b will be bigger and have a larger dif).
            if(arrA[i] < arrB[j]){
                i++;
            } else {
                j++;
            }
        }

        return answer;
    }

    // https://leetcode.com/problems/best-time-to-buy-and-sell-stock
    static int maxProfit(int[] prices) {
        // Brute force: calc the max profit you can get if you bought it on day x. Do it for all the days. O(n^2) time.
        // int maxProfit = 0;
        // for (int i = 0; i < prices.length - 1; i++) {
        //     for (int j = i+1; j < prices.length - 1; j++) {
        //         if(maxProfit < (prices[j] - prices[i]))
        //             maxProfit = prices[j] - prices[i];
        //     }
        // }
        //
        // return maxProfit;

        // Do it logically in time. Min is price at day one.
        // If there's a chance to buy it cheaper, do it. Each time it goes up, see if that max profit beats your old one.
        if(prices.length <= 1) return 0;

        int maxProfit = 0;
        int min = prices[0];

        for (int i = 1; i < prices.length; i++) {
            if(prices[i] < min)
                min = prices[i];
            else if( prices[i] - min > maxProfit)
                maxProfit = prices[i] - min;
            else
                ; // do nothing if price didn't fall or if the max profit is not greater than the previously obtainable
        }

        return maxProfit;
    }

}   // End ArrayQuestions class
