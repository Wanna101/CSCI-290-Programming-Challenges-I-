import java.util.*;

public class fzbz {
	
	// read in input, the first being fizz, 2nd buzz, etc.
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int fizz = in.nextInt();
		int buzz = in.nextInt();
		int range = in.nextInt();
		
		// if statement chain if the mods of fizz and buzz == 0 etc.
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
				// printing range if does not get
				// Fizz, Buzz, or FizzBuzz
				System.out.println(i);
			}
			
		}
		in.close();
		
	}

}
