import java.util.*;

public class FlexibleSpaces {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int width = in.nextInt();
        int numberOfPartitions = in.nextInt();
        int partition = 0;

        Vector<Integer> partitions = new Vector<Integer>();
        partitions.add(0);
        boolean[] options = new boolean[width + 1];

        for (int i = 0; i < numberOfPartitions; i++) {
            partitions.add(in.nextInt());
        }
        partitions.add(width);
        
        for (int i = 0; i < partitions.size(); i++) {
            for (int j = i + 1; j < partitions.size(); j++) {
                options[partitions.get(j) - partitions.get(i)] = true;
            }
        }
        
        for (int i = 1; i <= width; i++) {
            if(options[i]) {
                System.out.print(i + " ");  
            }
            
        }
    }
}