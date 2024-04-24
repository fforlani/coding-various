import java.util.LinkedList;
import java.util.List;

class Deamon {

    int Sconsumed;
    int Twait;
    int Srecovered;
    int Nfragment;
    List<Integer> fragments;

    int position;
    int maxFragment;

    Deamon(int el1, int el2, int el3, int el4, List<Integer> l, int pos){
        Sconsumed = el1;
        Twait = el2;
        Srecovered = el3;
        Nfragment = el4;
        fragments = l;

        position = pos;
        maxFragment = fragments.stream().mapToInt(Integer::intValue).sum();
    }

    int getCollectionableFragment (int tRemaining){
        return (tRemaining >= Nfragment ?
                maxFragment : fragments.subList(0, tRemaining).stream().mapToInt(Integer::intValue).sum());
    }

    double defineStaminaQuality(){
        return (double) (Srecovered-Sconsumed)/ (double) Twait;
    }

    double defineQuality(int tRemaining){
        return Math.sqrt(getCollectionableFragment(tRemaining))*defineStaminaQuality();
    }

    double defineQualityV2(int tRemaining){
        return (double) getCollectionableFragment(tRemaining)/Game.maxFragmentNumber.getAsInt()*defineStaminaQuality()/Game.maxStaminaQuality.getAsDouble();
    }
}
