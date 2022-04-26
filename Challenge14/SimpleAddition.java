import java.util.*;
import java.math.*;

// LINK: https://open.kattis.com/problems/simpleaddition

public class SimpleAddition {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String one = input.nextLine();
		String two = input.nextLine();

		BigInteger numberOne = new BigInteger(one);
		BigInteger numberTwo = new BigInteger(two);
		BigInteger sum = numberOne.add(numberTwo);
		System.out.println(sum);
	}
}
