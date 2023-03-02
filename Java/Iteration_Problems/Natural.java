import java.util.Scanner;

public class Natural {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = sc.nextInt(), sum = 0;
        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }
    }
}
