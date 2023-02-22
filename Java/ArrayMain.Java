public class ArrayMain{
    public static void main(String[] args){
        int[] arr = {1,2,3,4,5};
        printArray(arr);
        System.out.println("Largest: " + getLargest(arr));
        System.out.println("Smallest: " + getSmallest(arr));
        System.out.println("Sum: " + getSum(arr));
        System.out.println("Average: " + getAverage(arr));
        System.out.println("Index of largest: " + getIndexOfLargest(arr));
        System.out.println("Index of smallest: " + getIndexOfSmallest(arr));
        System.out.println("Reversed: " + reverse(arr));
    }
  
    public static void printArray(int[] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }
    }
  
    public static int getLargest(int[] arr){
        int largest = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > largest){
                largest = arr[i];
            }
        }
        return largest;
    }

    public static int getSmallest(int[] arr){
        int smallest = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < smallest){
                smallest = arr[i];
            }
        }
        return smallest;
    }

    public static int getSum(int[] arr){
        int sum = 0;
        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
        }
        return sum;
    }

    public static double getAverage(int[] arr){
        int sum = getSum(arr);
        return (double)sum / arr.length;
    }

    public static int getIndexOfLargest(int[] arr){
        int largest = arr[0];
        int index = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > largest){
                largest = arr[i];
                index = i;
            }
        }
        return index;
    }

    public static int getIndexOfSmallest(int[] arr){
        int smallest = arr[0];
        int index = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < smallest){
                smallest = arr[i];
                index = i;
            }
        }
        return index;
    }

    public static int[] reverse(int[] arr){
        int first = 0, last = arr.length - 1, temp;
        while(first < last){
            temp = arr[first];
            arr[first] = arr[last];
            arr[last] = temp;
            first++;
            last--;
        }
        return reversed;
    }
}
