import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {    
    

    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st= new StringTokenizer(br.readLine());
    	int n = Integer.parseInt(st.nextToken());
    	int m = Integer.parseInt(st.nextToken());
    	int[] arr = new int[n];
    	StringTokenizer st2 = new StringTokenizer(br.readLine());
    	HashMap<Integer, Integer> h = new HashMap<>();
    	for(int i=0; i<n; i++) {
    		arr[i] = Integer.parseInt(st2.nextToken());
    		int value = h.getOrDefault(arr[i], 0);
    		h.put(arr[i], value+1);
    	}
    	
    	StringTokenizer st3 = new StringTokenizer(br.readLine());
    	for(int i =0; i<m; i++) {
    		int find_value = Integer.parseInt(st3.nextToken());
    		System.out.print(h.getOrDefault(find_value, 0)+ " ");
    	}
    	
    }
}
