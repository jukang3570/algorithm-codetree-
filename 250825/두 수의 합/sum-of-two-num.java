import java.util.HashMap;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
        int n = sc.nextInt();
        int k = sc.nextInt();
        int cnt = 0;
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
            h.put(i,arr[i]);
        }
        // Please write your code here.
        for(int i = 1; i<n ;i++) {
        	for(int j= i+1; j<=n ;j++) {
        		if(h.getOrDefault(i, 0) + h.getOrDefault(j, 0) == k) {
        			cnt++;
        		}
        	}
        }
        
        System.out.println(cnt);
    }
}