import java.util.*;

public class LineThem2 {
	
	public static boolean inc = false;
	public static boolean dec = false;	
	
	public static void recursive(int i, ArrayList<String> strings) {
		if (i >= strings.size() - 1) {
			return;
		}
		if (strings.get(i).compareTo(strings.get(i + 1)) < 0) {
			dec = true;
		} else {
			inc = true;
		}
		recursive(i + 1, strings);
	}
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int number = Integer.parseInt(in.nextLine());
		
		ArrayList<String> strings = new ArrayList<String>();
		
		for (int i = 0; i < number; i++) {
			String s = in.nextLine();
			strings.add(s);
		}

		recursive(0, strings);

		if (inc == true && dec == true) {
			System.out.println("NEITHER");
		} else if (inc == false) {
			System.out.println("INCREASING");
		} else {
			System.out.println("DECREASING");
		}
	}

}
