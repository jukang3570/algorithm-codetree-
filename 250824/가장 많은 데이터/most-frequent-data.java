import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {    
    

    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	int ans = 0;
    	HashMap<String, Integer> h = new HashMap<String, Integer>();
    	for(int i =0; i<n ; i++) {
    		String Line = br.readLine();
    		int cnt = h.getOrDefault(Line, 0);
    		h.put(Line, cnt+1);
    		ans = Math.max(ans, cnt+1);
    	}
    	
    	System.out.println(ans);
    }
}
