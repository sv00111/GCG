import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Obj {


	ArrayList<String> rules = new ArrayList<>(Arrays.asList("1", "2"));

	Random rand = new Random();

	Subject sub = new Subject();
	PlSubject plSub = new PlSubject();


	public String pick(ArrayList<String> words)  {
		String word = words.get(rand.nextInt(words.size()));
		return word;
	}

	public String generate() {
		String str = null;
		String rule = pick(rules);
		switch(rule) {
		case "1":
			str = sub.generate();
			break;
		case "2":
			str = plSub.generate();
			break;

		}
		return str;

	}

}
