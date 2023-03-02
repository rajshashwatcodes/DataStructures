import java.util.*;

public class Fibonacci {
    public static void main (String args[]){
        Scanner sc =  new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt(), a = 0, b = 1,c=0;
        System.out.println(0);
        System.out.println(1);
        for (int i = 2; i < n; i++){
            System.out.println(a+b);
            if (i % 2 != 0) 
                a = a+b;
            else
                b = a+b;
        }
    }
}
