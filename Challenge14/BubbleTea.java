import java.util.*;
import java.math.*;

// LINK: https://open.kattis.com/problems/bubbletea

public class BubbleTea {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int numTeas = input.nextInt();
		int[] teaPrices = new int[numTeas];
		for (int i = 0; i < numTeas; i++) {
			teaPrices[i] = input.nextInt();
		}

		int numToppings = input.nextInt();
		int[] toppingPrices = new int[numToppings];
		for (int i = 0; i < numToppings; i++) {
			toppingPrices[i] = input.nextInt();
		}

		int smallestPrice = 2147483647;
		for (int i = 0; i < numTeas; i++) {
			int firstNum = input.nextInt();
			while (firstNum != 0) {
				int nextNum = input.nextInt();
				if (teaPrices[i] + toppingPrices[nextNum - 1] < smallestPrice) {
					smallestPrice = teaPrices[i] + toppingPrices[nextNum - 1];
				}
				firstNum--;
			}
		}

		int money = input.nextInt();
		// minus one for the teacher
		int totalTeas = (money / smallestPrice) - 1;
		// floor number if negative
		if (totalTeas < 0) {
			totalTeas = 0;
		}
		System.out.println(totalTeas);

	}
}
