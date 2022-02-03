import java.util.*;

public class fzbz {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int fizz = in.nextInt();
		int buzz = in.nextInt();
		int range = in.nextInt();
		
		for (int i = 1; i <= range; i++) {
			if (i % fizz == 0 && i % buzz == 0) {
				System.out.println("FizzBuzz");
			}
			else if (i % fizz == 0) {
				System.out.println("Fizz");
			} 
			else if (i % buzz == 0) {
				System.out.println("Buzz");
			} else {
				System.out.println(i);
			}
			
		}
		in.close();
		
	}

}
