import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args){
        Scanner in =new Scanner(System.in);
        int T=in.nextInt();
        for(int i=1;i<=T;i++){
            int N=in.nextInt(), B=in.nextInt();
            int[] A=new int[N];
            for(int j=0;j<N;j++)
                A[j]=in.nextInt();
            Arrays.sort(A);
            int speso=0, n=0;
            while(n<N && speso+A[n]<=B){
                speso+=A[n];
                n++;
            }
            System.out.println("Case #"+i+": "+n);
        }
    }
}