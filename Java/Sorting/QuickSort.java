import java.util.*;
public class QuickSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Quick Sort Test\n");
        int n, i;
        System.out.println("Enter number of integer elements");
        n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("\nEnter " + n + " integer elements");
        for (i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n - 1);
        System.out.println("\nElements after sorting ");
        for (i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
        sc.close();

    }
    
    int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }
    void sort(int arr[], int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }
}
