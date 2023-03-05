import java.util.Scanner;

public class PrintArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the array length: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        printArr(arr,n-1);
    }

    public static int printArr(int[] arr,int n) {
        if (n == -1) 
            return 0;
        printArr(arr,n-1);
        System.out.println(arr[n]); 
        return n;
    }
}
