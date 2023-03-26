package Sep27;
import java.util.*;

public class MagicSquare {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n,sumr=0,sumc=0,sumd=0,sumd2=0,sum=0,flag = 0,c=1;
		System.out.println("Enter the size of matrix");
		n = sc.nextInt();
		int arr[][] = new int[n][n];
		System.out.println("Enter the matrix");
		for (int i = 0; i< n; i++) {
			for (int j = 0; j< n; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		for (int j = 0; j< n; j++) {
			sum += arr[0][j];
		}
		for (int i = 0; i< n; i++) {
			for (int j = 0; j< n; j++) {
				sumr += arr[i][j];
				sumc += arr[j][i];
				if (i == j) {
					sumd += arr[i][j];
				}
			}
			sumd2 += arr[i][n-c];
			System.out.println(sumd2);
			c+=1;
			if (sum != sumc || sum != sumr ) {
				flag = 0;
			}
			else {
				flag = 1;
			}	
			}
		if (flag != 1) {
			System.out.println(sum);
			System.out.println(sumd2);
			if ((sum == sumd) && (sum == sumd2)) {
				
				System.out.println("Magic Square");
			}
			else {
				System.out.println("Not Magic Square");
			}
			
		}
	}

}
