import java.util.Arrays;
        import java.util.Collections;
        import java.util.Scanner;

public class Solution {

    static int R,C;
    public static void main(String[] args){
        Scanner reader = new Scanner(System.in);
        int T=reader.nextInt();
        int[] sol=new int[T];
        for (int i=1;i<=T;i++){
            R=reader.nextInt();
            C=reader.nextInt();
            int[][] H=new int[R][C];
            int[][] W=new int[R][C];
            for (int j=0;j<R;j++)
                for(int k=0;k<C;k++){
                    H[j][k]=reader.nextInt();
                    W[j][k] = isEdge(j, k) ? H[j][k] : Integer.MAX_VALUE;
                }
            int update=1;
            while(update==1){
                update=0;
                for (int j=1;j<R-1;j++){
                    for(int k=1;k<C-1;k++){
                        int w= Collections.min(Arrays.asList(W[j-1][k], W[j+1][k], W[j][k-1], W[j][k+1]));
                        w=Math.max(w,H[j][k]);
                        if(w!=W[j][k]) {
                            update=1;
                            W[j][k]=w;
                        }
                    }
                }
            }
            for (int j=0;j<R;j++)
                for(int k=0;k<C;k++)
                    sol[i-1]+=W[j][k]-H[j][k];
        }
        for (int i=1;i<=T;i++)
            System.out.println("Case #"+i+": "+sol[i-1]);
    }

    private static boolean isEdge(int i, int j){
        return i == 0 || i == R - 1 || j == 0 || j == C - 1;
    }
}
