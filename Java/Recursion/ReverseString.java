import java.util.*;

public class ReverseString {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String: ");
        String s = sc.nextLine();
        printReverse(s);
    }

    public static String printReverse(String s){
        
        if (s.length()  == 0)
            return s;
        System.out.print(s.charAt(s.length()-1));
        String X = s.substring(0,s.length()-1);
        printReverse(X);
        return s;
    }
}