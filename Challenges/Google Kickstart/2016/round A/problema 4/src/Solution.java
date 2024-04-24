/*
    Il codice seguente da le risposte corrette nei due esempi riportati da google, ma non passa nessuno dei due dataset per TLE (time limit excepiton)
    credo che in realtà il problema sia maggiormente la memoria utilizza per fare tutte le varie copie per i meccanismi ricorsivi.
    L'algoritmo creo che sia comunque giusto e la sua logica è:
    -creare una lista delle carte disponibili e calcolare tutte le possibili combinazioni di 8 elementi delle date carte
    -per ciascuna combinazione calcolare quale sia la configurazione, entro i limiti delle monete, che garantisca maggiore potere d'attacco e restituire tale
     potere nel caso migliore. Per fare ciò si prende in considerazione il migliore upgrade (rapporto incremento potenza e costo) e si verifica quale sia la
     massima potenza raggiungibile nel caso si faccia l'upgrade o meno
    -bisogna infatti migliorare questa ultima cosa evitando di controllare tutte le possibili combinazioni facendo delle potature dei vari rami

    Sotto c'è inoltre il codice commentato di un altra persona, che passa con successo il dataset 1 ma non il seocndo causa tempo. Viene utilizzato un algoritmo
    dfs (ricerca in profondità) che pero non ho capito come funzioni
 */

import java.util.*;

public class Solution {

     class Card {
         boolean toUpdate;
         int k, l;
         int[] a, c;
         Card(int _k, int _l, boolean _toUpdate) {
            k=_k;l=_l;toUpdate=_toUpdate;
            a=new int[k+1];
            c=new int[k];
         }
    }

    public static void main (String[] args){
        Scanner in =new Scanner(System.in);
        int T=in.nextInt();
        for(int i=1;i<=T;i++){
            System.out.println("Case #"+i+": "+new Solution().solve(in));
        }
    }

    private int solve(Scanner in) {
        int m=in.nextInt();
        int n=in.nextInt();
        Card[] cards=new Card[n];
        for (int i=0;i<n;i++) {
            cards[i]=new Card(in.nextInt(), in.nextInt(),true);
            int k=cards[i].k;
            for (int j=1;j<=k;j++)
                cards[i].a[j]=in.nextInt();
            for (int j=1;j<k;j++)
                cards[i].c[j]=in.nextInt();
        }
        List<List<Card>> comb=getCombination(Arrays.asList(cards),8);
        int maxPower=0;
        for(List<Card> list : comb){
            List<Card> copy=copy(list);
            getBestUpdate(m,copy);
            maxPower=Math.max(maxPower,getBestUpdate(m,copy));
        }
        return maxPower;
    }

    private List<Card> copy(List<Card> cards){
         List<Card> list=new LinkedList<>();
         for(Card c:cards){
             Card card=new Card(c.k,c.l,c.toUpdate);
             for (int i=1;i<=c.k;i++)
                 card.a[i]=c.a[i];
             for (int i=1;i<c.k;i++)
                 card.c[i]=c.c[i];
             list.add(card);
         }
         return list;
    }

    private int getPower(List<Card> cards){
        int power=0;
        for(Card c:cards)
            power+=c.a[c.l];
        return power;
    }

    private int getBestUpdate(int m, List<Card> cards){
         List<Card> subList=new LinkedList<>();
         for(Card c:cards)
             if(c.toUpdate)
                 subList.add(c);
         if(m==0||subList.size()==0)
             return getPower(cards);
         boolean con=false;
         for(Card c:subList)
             if(c.l!=c.k&&c.c[c.l]<=m)
                    con=true;
         if(!con){
             return getPower(cards);
         }
         float rate=0;
         int index=-1;
         for (Card c : subList) {
            if (c.l == c.k || c.c[c.l] > m)
                continue;
            float r = ((float) (c.a[c.l + 1] - c.a[c.l])) / ((float) c.c[c.l]);
            if (r > rate) {
                index = cards.indexOf(c);
                rate = r;
            }
        }
         List<Card> copy1=copy(cards);
         copy1.get(index).l++;
         int p1=getBestUpdate(m-copy1.get(index).c[copy1.get(index).l-1],copy1);

         List<Card> copy2=copy(cards);
         copy2.get(index).toUpdate=false;
         int p2=getBestUpdate(m,copy2);
         return Math.max(p1,p2);
    }

    private  <T> List<List<T>> getCombination(List<T> values, int size) {

        if (0 == size)
            return Collections.singletonList(Collections.emptyList());

        if (values.isEmpty())
            return Collections.emptyList();

        List<List<T>> combination = new LinkedList<>();

        T actual = values.iterator().next();

        List<T> subSet = new LinkedList<T>(values);
        subSet.remove(actual);

        List<List<T>> subSetCombination = getCombination(subSet, size - 1);

        for (List<T> set : subSetCombination) {
            List<T> newSet = new LinkedList<T>(set);
            newSet.add(0, actual);
            combination.add(newSet);
        }

        combination.addAll(getCombination(subSet, size));

        return combination;
    }
}


//import java.util.*;
//
///**
// * APAC 2017 Round A Problem D: Clash Royale
// * Check README.md for explanation.
// */
//public class Solution {
//
//    class Card {
//        int k, l;
//        long[] a, c;
//        public Card(int _k, int _l) {
//            k=_k;l=_l;
//            a=new long[k+1];
//            c=new long[k+1];
//        }
//    }
//
//    private String solve(Scanner scanner) {
//        long m=scanner.nextLong();
//        int n=scanner.nextInt();
//        Card[] cards=new Card[n];
//        long[] maxAtk=new long[n];
//        for (int i=0;i<n;i++) {
//            cards[i]=new Card(scanner.nextInt(), scanner.nextInt());
//            int k=cards[i].k;
//            for (int j=1;j<=k;j++) {
//                cards[i].a[j]=scanner.nextLong();
//            }
//            for (int j=1;j<k;j++) {
//                cards[i].c[j]=scanner.nextLong();
//            }
//            maxAtk[i]=(i==0?0:maxAtk[i-1])+cards[i].a[cards[i].k];
//        }
//        dfs(m, n-1, cards, Math.min(n, 8), 0, maxAtk);
//        return String.valueOf(result);
//    }
//
//    private long result=0;
//
//    private void dfs(long m, int n, Card[] cards, int remain, long current, long[] maxAtk) {
//        if (n<0 || remain==0) {
//            if (current>result) result=current;
//            return;
//        }
//        // prune
//        if (current+maxAtk[n]<=result) return;
//        dfs(m, n-1, cards, remain, current, maxAtk);
//        Card card=cards[n];
//        dfs(m, n-1, cards, remain-1, current+card.a[card.l], maxAtk);
//        long need=0;
//        for (int i=card.l+1;i<=card.k;i++) {
//            need+=card.c[i-1];
//            if (m<need) break;
//            dfs(m-need, n-1, cards, remain-1, current+card.a[i], maxAtk);
//        }
//    }
//
//    public static void main(String[] args) throws Exception {
//        //System.setOut(new PrintStream("E:\\desktop\\output.txt"));
//        Scanner scanner=new Scanner(System.in);
//        int times=scanner.nextInt();
//        long start=System.currentTimeMillis();
//        for (int t=1;t<=times;t++) {
//            System.out.println(String.format("Case #%d: %s", t, new Solution().solve(scanner)));
//        }
//        long end=System.currentTimeMillis();
//        System.err.println(String.format("Time used: %.3fs", (end-start)/1000.0));
//
//    }
//
//}