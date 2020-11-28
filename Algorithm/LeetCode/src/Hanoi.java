public class Hanoi {

    private static void hanoi(int n, char a, char b, char c) {

        if (n == 1) {
            System.out.println(a + "-> " + c);
        } else {
            hanoi(n - 1, a, c, b);
            System.out.println(a + "-> " + c);
            hanoi(n - 1, b, a, c);
        }
    }

    public static void main(String[] args) {

        /**
         * a-> c
         * a-> b
         * c-> b
         * a-> c
         * b-> a
         * b-> c
         * a-> c
         */
        hanoi(3, 'a', 'b', 'c');
    }
}
