import java.util.Scanner;

public class Solution {

    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        int T=in.nextInt();
        for(int i=1;i<=T;i++){
            int N=in.nextInt(), K=in.nextInt(), P=in.nextInt();
            int[] stack=new int[K];
            int[][] dp=new int[N+1][P+1];
            for(int j=0;j<N;j++){
                for(int k=0;k<K;k++)
                    stack[k]=in.nextInt();
                for(int k=1;k<K;k++)
                    stack[k]+=stack[k-1];
                for(int a=0;a<=P;a++){
                    for(int b=1;b<=Math.min(K,a);b++)
                        dp[j+1][a]=Math.max(dp[j][a],Math.max(dp[j+1][a],dp[j][a-b]+stack[b-1]));
                }
            }
            System.out.println("Case #"+i+": "+dp[N][P]);
        }
    }
}
