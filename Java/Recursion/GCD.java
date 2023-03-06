import java.util.Scanner;

public class GCD {
    public static void main (String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the 1st number: ");
        int n1 = sc.nextInt();
        System.out.println("Enter the 2nd number: ");
        int n2 = sc.nextInt(),gcd;
        if ( n1 > n2)
            gcd = HCF(n1,n2);
        else 
            gcd = HCF(n1,n2);
        System.out.println(gcd);
    }

    public static int HCF(int n1,int n2){
        if (n2 == 0){
            return n1;
        }
        return HCF(n2,n1%n2);
    }
}
