import java.util.Scanner;

public class PowerXYR {
    public static void main (String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the base: ");
        int X = sc.nextInt();
        System.out.println("Enter the power: ");
        int y = sc.nextInt();
        int exp = power(X,y);
        System.out.println(exp);
    }

    public static int power(int X, int y){
        if (y == 1){
            return X;
        }
        return X * power(X, y-1);
    }
}
