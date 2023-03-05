import java.util.Scanner;

public class NaturalSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = sc.nextInt();
        int sum = sumNatural(n);
        System.out.println(sum);
    }

    public static int sumNatural(int n) {
        if (n == 1) {
            return 1;
        } else {
            return n + sumNatural(n - 1);
        }
    }
}
