import java.util.*;

public class ReverseNumber {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Number: ");
        int s = sc.nextInt(), r=0;
        while (s > 0){
            r = r * 10 + s % 10 ;
            s = s/10;
        }
        System.out.println(r);
    }
}
