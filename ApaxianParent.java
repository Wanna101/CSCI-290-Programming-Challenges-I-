import java.util.*;
import java.io.*;

public class challenge {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in); 
		String one = in.next();
		String two = in.next();
		if (one.matches(".*[aeiou]$")) {
			System.out.println(one.substring(0, one.length() - 1) + "ex" + two);
		}
		else if (one.endsWith("ex")) {
			System.out.println(one + two);
		} else {
			System.out.println(one + "ex" + two);
		}
		
	}

}
