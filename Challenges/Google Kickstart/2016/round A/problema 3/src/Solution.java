import java.util.Scanner;

public class Solution {

    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        int T=in.nextInt();
        for(int i=1;i<=T;i++){
            int m=in.nextInt();
            int[] c=new int[m+1];
            for (int j=0;j<=m;j++)
                c[j]=in.nextInt();
            System.out.println("Case #"+i+": "+bisezione(c,m));
        }
    }

    private static double bisezione(int[] c,int m){
        double prec=1e-7;
        double a=-1;
        double b=1;
        double guess=0;
        while(b-a>prec){
            guess=(b+a)/2;
            double approx=-c[0]*Math.pow(1+guess,m+1);
            for(int i=1;i<=m;i++)
                approx+=c[i]*Math.pow(1+guess,m+1-i);
            if(approx<0)
                b=guess;
            else
                a=guess;
        }
        return guess;
    }
}
