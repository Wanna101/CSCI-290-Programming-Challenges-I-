import java.util.*;
import java.util.Arrays;


public class DigitsFunction {
	// formula for sum squared base
	public static int calculateAnswer(int n, int b) {
		int total = 0;
		while (n > 0) {
			int next = (n % b);
			total += (next * next);
			n = n / b;
		}
		return total;
	}
	# read in input and store in array
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int number = in.nextInt();
		String[] answers = new String[number];
		for (int i = 0; i < number; i++) {
			int one = in.nextInt();
			int two = in.nextInt();
			int three = in.nextInt();
			int answer = calculateAnswer(three, two);
			String newAns = Integer.toString(answer);
			answers[i] = newAns;
		}
		# loop through array to print answers
		for (int i = 0; i < number; i++) {
			System.out.println((i + 1) + " " + answers[i]);
		}
	}

}
