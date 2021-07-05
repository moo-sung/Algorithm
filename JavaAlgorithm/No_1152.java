package JavaAlgorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_1152 {
    public static void main(String[] args) throws Exception{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String s = input.readLine().trim();
        int c = 0;

        if (!s.equals("")){
            c = 1;
        }
        for (int i=0; i<s.length();i++){
            if(s.charAt(i) == ' '){
                c++;
            }
        }

        System.out.println(c);
        input.close();
    }
}
