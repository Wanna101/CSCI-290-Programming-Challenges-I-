import java.util.*;

public class Kornislav {
	// Complexity: This would be O(1), but due to the 
	// sort function from Arrays, it is O(nlog(n))

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int array[] = new int[4];
		for (int i = 0; i < 4; i++) {
			array[i] = input.nextInt();
		}
		Arrays.sort(array);
		System.out.println(array[0] * array[2]);
	}

}
