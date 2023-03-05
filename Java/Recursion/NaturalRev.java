import java.util.Scanner;

public class NaturalRev {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = sc.nextInt();
        Natural(n);
    }

    public static int Natural(int n) {
        if (n == 0) 
            return 0;
        Natural(n-1); 
        System.out.println(n);
       return n;
    }
} 
