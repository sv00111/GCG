import java.util.*;
import java.io.*;

public class GCG {
	public static void main(String[] args) {
		ArrayList adjList = loadDict("adjectives.txt");
		ArrayList advList = loadDict("adverbs.txt");
		ArrayList prepositionList = loadDict("prepositions.txt");
		System.out.println("adjectives:\n" + adjList);
	}

	private static ArrayList loadDict (String filename) {
		ArrayList list = new ArrayList();
		Scanner scan;
		try {
			scan = new Scanner (new File (filename));
		}
		catch (FileNotFoundException e) {
			System.out.println("Error: File not found: " + filename);
			return null;
		}
		while (scan.hasNextLine()) {
			list.add(scan.next());
		}
		return list;
	}
}