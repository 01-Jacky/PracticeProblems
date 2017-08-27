import java.util.*;

public class MatrixQuestions {
    static void run_demo() {
        int n = 3;
        int m = 3;
        int[][] matrix = new int[n][m];

        // Fill matrix
        int count = 1;
        for(int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matrix[i][j] = count++;
            }
        }
        printMatrix(matrix);

        //////////////// Testing printing recursively
        printMatrix_Recursive(matrix);

        //////////////// Testing rotations
        // System.out.println("After rotating right:\n");
        // rotateMatrix(matrix, true);
        // printMatrix(matrix);
        //

        // System.out.println("After rotating left:\n");
        // rotateMatrix(matrix, false);
        // printMatrix(matrix);


    }

    static void rotateMatrix(int[][] matrix, boolean clockwise) {
        // O(n*m) space method by copying each row to a temp
        int rotations = clockwise ? 1 : 3;

        for (int r = 0; r < rotations; r++){    // For rotation left or right
            // Main Rotation logic
            int rows = matrix.length;
            int column_i = matrix[0].length - 1;
            int[][] temp = new int[matrix.length][matrix[0].length];

            for (int row_i = 0; row_i < rows; row_i++) {                // Create the rotated array
                for (int i = 0; i < matrix.length; i++) {
                    temp[i][column_i] = matrix[row_i][i];
                }
                column_i--;
            }

            for (int i = 0; i < matrix.length; i++) {                   // Copy back over to original
                for (int j = 0; j < matrix[0].length; j++) {
                    matrix[i][j] = temp[i][j];
                }
            }
        }

        // swapping index solution
        // int layersToDo = width/2;
        //
        // for(layer to layersToDo){
        //     int last = width-1;
        //
        //     for(first = 0 to last){
        //         // store right
        //         // top to right
        //
        //         // store bottom
        //         // right to bottom
        //
        //         // store left
        //         // bottom to left
        //
        //         // left to top
        //
        //     }
        // }
    }

    // Print matrix
    static void printMatrix(int[][] m){
        for(int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[0].length; j++) {
                System.out.printf("%-3s", m[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }

    // Print matrix
    static void printMatrix_Recursive(int[][] m){
        printMatrix_helper(m,0);
        System.out.println();
    }

    static void printMatrix_helper(int[][] m, int row){
        // Base case
        if(row > m[0].length-1)
            return;

        // Print row and recursively call the next row
        for(int i = 0; i < m.length; i++){
            System.out.printf("%-3s", m[row][i]);
        }
        System.out.println();

        printMatrix_helper(m,row +1);
    }

    // Print Matrix in spiral order (layer by layer)
    //  https://leetcode.com/problems/spiral-matrix/
    // recursion solution: http://articles.leetcode.com/printing-matrix-in-spiral-order/
    public static List<Integer> spiralOrder(int[][] matrix) {
        return spiralOrderHelper(matrix, matrix.length, matrix[0].length);
    }

    private static List<Integer> spiralOrderHelper(int[][] matrix, int row, int column){
        List<Integer> list = new ArrayList<>();

        // Base cases
        // If matrix is empty
        // If only 1 element

        // Decompose, recursion, and combining result from recursion
        list.addAll(spiralOrderHelper(matrix, row+1, column-1));

        return list;
    }
}