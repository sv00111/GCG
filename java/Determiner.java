import java.util.ArrayList;
import java.util.Random;

public class Determiner {
	public Random rand = new Random();


	public String pick(ArrayList<String> words)  {
    	String word = words.get(rand.nextInt(words.size()));
    	return word;
  	}

	public String generate() {
		String str = pick(GCG.detList);
		return str;
		
	}
}