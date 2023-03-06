import java.util.*;

public class ReverseNumber {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Number: ");
        int n = sc.nextInt();
        printReverse(n);
    }

    public static int printReverse(int n){
        
        if (n  == 0)
            return n;
        System.out.print(n%10);
        printReverse(n/10);
        return n;
    }
}