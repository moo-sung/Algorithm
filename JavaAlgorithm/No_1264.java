package JavaAlgorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1264 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String s = "";
        String m = "aeouiAEOUI";

        while (true) {
            s=input.readLine();
            if(s.equals("#")){
                break;
            }
            int count = 0;
            for (int i = 0; i < s.length(); i++) {
                for (int j = 0; j < m.length(); j++) {
                    if(s.charAt(i)==(m.charAt(j))){
                        count++;
                    }
                }
            }
            System.out.println(count);
        }
        input.close();
    }
}
