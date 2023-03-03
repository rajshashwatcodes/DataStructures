import java.util.Scanner;

public class GCD {
    public static void main (String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the 1st number: ");
        int n1 = sc.nextInt(),r;
        System.out.println("Enter the 2nd number: ");
        int n2 = sc.nextInt(),gcd;
        if ( n2 > n1){
            int temp = n1;
            n1 = n2;
            n2 = temp;
        }
        while (n2 != 0){
            r = n1 % n2;
            n1 = n2;
            n2 = r;
        }
        System.out.println(n1);
    }
}
