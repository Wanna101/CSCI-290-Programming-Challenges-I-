import java.util.*;
import java.math.*;

public class AstrologicalSign {

	public static String zodiac(String line) {
		String[] split = line.trim().split("\\s+");
		String tmp = split[0];
		String month = split[1];
		Integer day = Integer.valueOf(tmp);
		String zodiacSign = "";

		if (month.equals("Mar")) {
			if (day < 21) zodiacSign = "Pisces";
			else zodiacSign = "Aries";
		} else if (month.equals("Apr")) {
			if (day < 21) zodiacSign = "Aries";
			else zodiacSign = "Taurus";
		} else if (month.equals("May")) {
			if (day < 21) zodiacSign = "Taurus";
			else zodiacSign = "Gemini";
		} else if (month.equals("Jun")) {
			if (day < 22) zodiacSign = "Gemini";
			else zodiacSign = "Cancer";
		} else if (month.equals("Jul")) {
			if (day < 23) zodiacSign = "Cancer";
			else zodiacSign = "Leo";
		} else if (month.equals("Aug")) {
			if (day < 23) zodiacSign = "Leo";
			else zodiacSign = "Virgo";
		} else if (month.equals("Sep")) {
			if (day < 22) zodiacSign = "Virgo";
			else zodiacSign = "Libra";
		} else if (month.equals("Oct")) {
			if (day < 23) zodiacSign = "Libra";
			else zodiacSign = "Scorpio";
		} else if (month.equals("Nov")) {
			if (day < 23) zodiacSign = "Scorpio";
			else zodiacSign = "Sagittarius";
		} else if (month.equals("Dec")) {
			if (day < 22) zodiacSign = "Sagittarius";
			else zodiacSign = "Capricorn";
		} else if (month.equals("Jan")) {
			if (day < 21) zodiacSign = "Capricorn";
			else zodiacSign = "Aquarius";
		} else if (month.equals("Feb")) {
			if (day < 20) zodiacSign = "Aquarius";
			else zodiacSign = "Pisces";
		}
		return zodiacSign;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String tmp = input.nextLine();
		Integer number = Integer.valueOf(tmp);

		String[] dates = new String[number];
		for (int i = 0; i < number; i++) {
			dates[i] = input.nextLine();
		}

		for (int i = 0; i < number; i++) {
			String zodiacSign = zodiac(dates[i]);
			System.out.println(zodiacSign);
		}
	}
}