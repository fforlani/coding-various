import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(reader.readLine());
        String[] leader=new String[T];
        for (int i=1;i<=T;i++){
            int N=Integer.parseInt(reader.readLine());
            int diff=0;
            leader[i-1]="";
            for(int j=1;j<=N;j++){
                String s=reader.readLine();
                int numChar=0;
                for(int k=0;k<s.length();k++){
                    if(s.charAt(k)!=' ' && !s.substring(0,k).contains(Character.toString(s.charAt(k))))
                        numChar++;
                }
                if(diff<numChar){
                  diff=numChar;
                  leader[i-1]=s;
                }else if(diff==numChar && s.compareTo(leader[i-1])<0)
                    leader[i-1]=s;
            }
        }
        for(int i=1;i<=T;i++)
            System.out.println("Case #"+i+": "+leader[i-1]);
    }
}
