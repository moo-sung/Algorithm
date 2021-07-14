package JavaAlgorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2511 {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int[] scoreA = new int[10];
        int[] scoreB = new int[10];
        
        StringTokenizer s = new StringTokenizer(input.readLine(), " ");


        for (int i = 0; i < 10; i++) {
            scoreA[i] = Integer.parseInt(s.nextToken());
        }

    }
}
