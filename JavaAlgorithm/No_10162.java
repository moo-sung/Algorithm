package JavaAlgorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_10162 {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int time = Integer.parseInt(input.readLine());
        int a = 300, b = 60, c = 10;
        if ((time % 10) == 0) {
            int buttonA = time / a;
            int buttonB = (time % a) / b;
            int buttonC = ((time % a) % b) / c;

            System.out.println(buttonA + " " + buttonB + " " + buttonC);
        } else {
            System.out.println("-1");
        }
    }
}
