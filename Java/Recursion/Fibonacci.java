import java.util.*;

public class Fibonacci {
    static int a = 0;
    static int b = 1;
    public static void main (String args[]){
        Scanner sc =  new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();
        if (n == 1)
            System.out.println(0);
        if (n >= 2){
            System.out.println(0);
            System.out.println(1);
        }
        printfibonacci(n-2);
    }

    public static int printfibonacci(int n){
        if (n == 0)
            return n;
        System.out.println(a+b);
        if (n % 2 != 0) 
            a = a+b;
        else
            b = a+b;
        printfibonacci(n-1);
            return n;
    }
}