import fanxing.MAN;
import fanxing.Animal;
import fanxing.Human;
import fanxing.WOMAN;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
//        List<? extends Human> list = new ArrayList<>();
////     【之前List中就有元素，不允许后添加，会导致类型不一致】添加受限，下面三个全错
//        list.add(new Human());//错误❌
//        list.add(new MAN());//错误❌
//        list.add(new Animal());//错误❌
//        list.add(new WOMAN());//错误❌
//
////        获取的只能是Human及其父类
//        MAN man = list.get(0);//错误❌
//        WOMAN woman = list.get(0);//错误❌
//        Human human = list.get(0);
//        Animal animal = list.get(0);
//
//        List<? super Human> list1 = new ArrayList<>();
//        list1.add(new WOMAN());
//        list1.add(new MAN());
//        list1.add(new Human());
//        list1.add(new Animal());//错误❌
//
////        获取受限【向下转型，如果没有强转就是错误】
//        MAN a_human1 = (MAN) list1.get(0);//抛出转型异常
//        Human human1 = (Human) list1.get(0);
//        Animal animal1 = (Animal) list1.get(1);
        Solution2 solution2=new Solution2();
        List<String> strings = solution2.generateParenthesis(1);
        System.out.println(strings);
        System.out.println(solution2.count);
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
