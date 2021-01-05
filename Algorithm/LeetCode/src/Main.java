import fanxing.MAN;
import fanxing.Animal;
import fanxing.Human;
import fanxing.WOMAN;

import java.util.ArrayList;
import java.util.List;

public class Main {
    static  Object lock=new Object();
    public static void main(String[] args) {
        Runnable runnable1=new Runnable() {
            @Override
            public void run() {
                while (true){
                    synchronized (lock){
                        System.out.println("A");

                        lock.notify();
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        };

        Runnable runnable2=new Runnable() {
            @Override
            public void run() {
                while (true){
                    synchronized (lock){
                        System.out.println("B");

                        lock.notify();
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        };

        Thread thread1=new Thread(runnable1);
        Thread thread2=new Thread(runnable2);
        thread1.start();
        thread2.start();
    }
}


class Solution2 {
    public int count=0;
    ArrayList<String> strings = null;
    public List<String> generateParenthesis(int n) {
        strings = new ArrayList<String>();
        generateParenthesis(n,0,0,"");
        return strings;
    }

    public void generateParenthesis(int n, int left, int right, String s){
        System.out.println("left="+left+" right= "+right);
        count++;
        if(left == n && right == n){
            strings.add(s);
            System.out.println(s);
            System.out.println(count);
            return;
        }
        if(left<n)
            generateParenthesis(n,left+1,right,s+"(");
        if(right<left)
            generateParenthesis(n,left,right+1,s+")");
    }
}


class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        // 参数校验
        if (matrix.length == 0) {
            return new int[0];
        }
        int row_count = matrix.length;
        int column_count = matrix[0].length;
        // 遍历次数/对角线条数
        int count = row_count + column_count - 1;
        int row = 0;
        int column = 0;
        // 出参
        int[] result = new int[row_count * column_count];
        int retIndex = 0;
        // 遍历次数
        for (int k = 0; k < count; k++) {
            if (k % 2 == 0) {
                // 从左到右往上遍历
                while (row >= 0 && column < column_count) {
                    result[retIndex] = matrix[row][column];
                    retIndex++;
                    row--;
                    column++;
                }

                // 数组越界，计算下次遍历开始坐标
                if (column < column_count) {
                    row = row + 1;
                } else {
                    row = row + 2;
                    column = column - 1;
                }
            } else {
                // 从右到左往下遍历
                while (row < row_count && column >= 0) {
                    result[retIndex] = matrix[row][column];
                    retIndex++;
                    row++;
                    column--;
                }
                // 数组越界，计算下次遍历开始坐标
                if (row < row_count) {
                    column = column + 1;
                } else {
                    row = row - 1;
                    column = column + 2;
                }
            }
        }
        return result;
    }
}
