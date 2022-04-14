	import java.util.*;

	public class Zoo {

		public static void main(String args[]) {
			Scanner in = new Scanner(System.in);
			// max amount of lists is 5
			int numLists = 0;

			do {
				// create new list and check items from input every time going through a list
				ArrayList<String> finalList = new ArrayList<String>();
				Map<String, Integer> check = new HashMap<String, Integer>();

				// read through the individual list and get number of Animals
				int numAnimals = Integer.parseInt(in.nextLine());
				if (numAnimals == 0) {
					break;
				}

				// iterate through the number of Animals
				for (int i = 0; i < numAnimals; i++) {
					// create array to hold single lines
					String[] animalName = in.nextLine().split(" ");
					// program reads through lowercase (i.e. White tiger and Tiger is a count of two) so use toLower
					// last word will be the type of animal so get last word
					animalName[animalName.length - 1] = animalName[animalName.length - 1].toLowerCase();
					// use map to check to see if it doesn't have animal yet
					if (!check.containsKey(animalName[animalName.length - 1])) {
						// add one to the animal type
						check.put(animalName[animalName.length - 1], 1);
						// add animal to final list
                    				finalList.add(animalName[animalName.length - 1]);
					} else {
						// add one to already instantiated type of animal
						check.replace(animalName[animalName.length - 1], check.get(animalName[animalName.length - 1]) + 1);
					}
				}
				numLists++;
				Collections.sort(finalList);
				System.out.println("List " + numLists + ":");

				for (String animal: finalList) {
					System.out.println(animal + " | " + check.get(animal));
				}		
			} while (numLists != 0);
		}
	}
