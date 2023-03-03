import java.util.*;

public class PowerXY {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter base value: ");
        int X = sc.nextInt();
        System.out.println("Enter power value: ");
        int y = sc.nextInt(), pow = 1;
        for (int i = 0; i < y; i++){
            pow = X * pow;
        }
        System.out.println(pow);
    } 
}
