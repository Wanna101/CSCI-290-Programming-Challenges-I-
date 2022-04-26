import java.util.*;
import java.math.*;

public class DigitProduct {

	public static String routine(String number) {
		int total = 1;
		number = number.replace("0", "");
		int[] numbers = new int[number.length()];

		Integer num = Integer.valueOf(number);
		for (int i = 0; i < number.length(); i++) {
			numbers[i] = num % 10;
			num = num / 10;
		}
		for (int i = 0; i < number.length(); i++) {
			total = total * numbers[i];
		}
		numbers = null;
		number = Integer.toString(total);
		number = number.replace("0", "");
		if (!(number.length() == 1)) {
			return routine(number);
		}
		return number;
	}


	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String number = input.nextLine();
		System.out.println(routine(number));
	}
}