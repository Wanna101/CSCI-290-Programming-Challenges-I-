import java.util.Scanner;


public class formula {
	


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// read in input
		Scanner in = new Scanner(System.in);
		int numberPoints = in.nextInt();
		// int number = Integer.parseInt(numberPoints);
		// System.out.println(number);
		
		// measurements to hold last loop's value
		// for calculation
		double last_one = -100000;
		double last_two = 0;
		double total = 0;
		for (int i = 0; i < numberPoints; i++) {
			double one = in.nextDouble();
			double two = in.nextDouble();
			// System.out.println(one);
			// System.out.println(two);
			if (last_one == -100000) {
				last_one = one; 
				last_two = two; 							
				continue;
			}
			// calculate trapezoid
			last_two = (last_two + two) / 2;
			last_one = (one - last_one);
			double calculation = last_one * last_two;
			calculation /= 1000;
			total += calculation;
			
			
			
			last_one = one;
			last_two = two;
		}
		System.out.println(total);
	}

}
