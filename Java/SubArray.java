public class SubArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] subArr = getSubArray(arr, 2, 5);
        printArray(subArr);
    }
    public static int[] getSubArray(int[] arr, int start, int end){
        int[] subArr = new int[end - start + 1];
        for(int i = start; i <= end; i++){
            subArr[i - start] = arr[i];
        }
        return subArr;
    }
    public static void printArray(int[] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }
    }
}
