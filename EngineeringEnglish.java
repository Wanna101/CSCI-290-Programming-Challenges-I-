import java.util.*;

public class EngineeringEnglish {
	// Complexity: O(n) because of the while loop

	// want uniqueness so use set to store words
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Set<String> unique = new HashSet<String>();
		String word = "";
		while(input.hasNext()) {
			word = input.next();
			
			// check to see if set contains duplicates even in the lower case
			if (unique.contains(word.toLowerCase())) {
				System.out.print(". ");
			}
			else {
				unique.add(word.toLowerCase());
				System.out.print(word + " ");
			}
		}
	}

}