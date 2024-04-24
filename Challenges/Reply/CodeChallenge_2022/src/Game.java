import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static sun.swing.MenuItemLayoutHelper.max;

class Game {

    private int Si = -1;
    private int Smax = -1;
    private int T = -1;
    private int D = -1;

    private int[] Sconsumed = {};
    private int[] Twait = {};
    private int[] Srecovered = {};
    private int[] Nfragment = {};
    private List<List<Integer>> fragments = new LinkedList<>();

    static OptionalDouble maxStaminaQuality;
    static OptionalInt maxFragmentNumber;

    private List<Deamon> deamons= new LinkedList<>();

    Game(String inputFile){
        parseInputV2(inputFile);

        maxStaminaQuality = deamons.stream().mapToDouble(Deamon::defineStaminaQuality).max();
        maxFragmentNumber = deamons.stream().mapToInt(d -> d.maxFragment).max();

        List<Deamon> match = solve();
        System.out.println(calculateRewardV2(match));
        createOutputFile(match, inputFile);
    }

    private List<Deamon> solve (){
        List<Deamon> match = new LinkedList<>();
        List<Integer> tPerDeamon = new LinkedList<>();

        // to define the order of the deamons i simulate a game
        int maxDeamon = Math.min(T, D);
        int stamina = Si;
        for (int t = 0; t<T ; t++){
            int tRemaining = T-t;

            // updating stamina
            for (int i = 0; i<match.size() ; i++){
                int turnPassed = t-tPerDeamon.get(i);
                if (turnPassed == match.get(i).Twait)
                    stamina = Math.min(Smax, stamina + match.get(i).Srecovered);
            }

            int finalStamina = stamina;
            List<Deamon> challengers = deamons.stream().filter(d -> d.Sconsumed <= finalStamina).collect(Collectors.toList());
            if (challengers.size() == 0)
                continue;
//            Deamon best = Collections.max(challengers, Comparator.comparing(d -> d.getCollectionableFragment(tRemaining)));
            Deamon best = Collections.max(challengers, Comparator.comparing(d -> d.defineQuality(tRemaining)));
            if (stamina - best.Sconsumed < Smax/10)
                best = Collections.max(challengers, Comparator.comparing(Deamon::defineStaminaQuality));
            match.add(best);
            tPerDeamon.add(t);
            deamons.remove(best);
        }
        return match;
    }

    private int calculateRewardV2(List<Deamon> match){
        int reward = 0;
        int currentDeamon = 0;
        List<Integer> tPerDeamon = new LinkedList<>();
        for (int t = 0; t < T; t++){
            // updating stamina
            for (int i = 0; i<Math.min(currentDeamon, match.size()) ; i++){
                int turnPassed = t-tPerDeamon.get(i);
                if (turnPassed == match.get(i).Twait)
                    Si = Math.min(Smax, Si + match.get(i).Srecovered);
            }
            if (currentDeamon < match.size() && Si >= match.get(currentDeamon).Sconsumed) {
                // can battle
                tPerDeamon.add(t);
                Si -= match.get(currentDeamon).Sconsumed;
                currentDeamon++;
            }
            //adding rewards
            for (int i = 0; i<Math.min(currentDeamon, match.size()) ; i++){
                int turnPassed = t-tPerDeamon.get(i);
                if (turnPassed < match.get(i).Nfragment)
                    reward += match.get(i).fragments.get(t-tPerDeamon.get(i));
            }
//            System.out.println(reward);
        }
        return reward;
    }

    private int calculateReward(int[] deamons){
        int reward = 0;
        int currentDeamon = 0;
        List<Integer> tPerDeamon = new LinkedList<>();
        for (int t = 0; t < T; t++){
            // updating stamina
            for (int i = 0; i<currentDeamon ; i++){
                int turnPassed = t-tPerDeamon.get(i);
                if (turnPassed == Twait[deamons[i]])
                    Si = Math.min(Smax, Si + Srecovered[deamons[i]]);
            }
            if (currentDeamon < deamons.length && Si >= Sconsumed[deamons[currentDeamon]]) {
                // can battle
                tPerDeamon.add(t);
                Si -= Sconsumed[deamons[currentDeamon]];
                currentDeamon++;
            }
            //adding rewards
            for (int i = 0; i<currentDeamon ; i++){
                int turnPassed = t-tPerDeamon.get(i);
                if (turnPassed < Nfragment[deamons[i]])
                    reward += fragments.get(deamons[i]).get(t-tPerDeamon.get(i));
            }
            System.out.println(reward);
        }
        return reward;
    }

    private void createOutputFile(List<Deamon> match, String inputFile){
        String filename = "./output/out"+inputFile.substring(0,2)+".txt";
        try {
            PrintWriter writer = new PrintWriter(filename, "UTF-8");
            for (Deamon deamon : match)
                writer.println(deamon.position);
            writer.close();
        } catch (FileNotFoundException | UnsupportedEncodingException e) { e.printStackTrace(); }
    }

    private void parseInputV2 (String inputFile){
        try {
            BufferedReader br = new BufferedReader(new FileReader(new File("./input/"+inputFile)));

            String[] header = br.readLine().split(" ");
            Si = Integer.parseInt(header[0]);
            Smax = Integer.parseInt(header[1]);
            T = Integer.parseInt(header[2]);
            D = Integer.parseInt(header[3]);

            String row;
            int number = 0;
            while ((row = br.readLine()) != null){
                String[] values = row.split(" ");
                deamons.add(new Deamon(Integer.parseInt(values[0]),
                        Integer.parseInt(values[1]),
                        Integer.parseInt(values[2]),
                        Integer.parseInt(values[3]),
                        Arrays.asList(values).subList(4, values.length)
                                .stream().map(Integer::parseInt)
                                .collect(Collectors.toList()),
                        number));
                number++;
            }
        } catch (IOException e) { e.printStackTrace(); }
    }

    private void parseInput (String inputFile){
        try {
            BufferedReader br = new BufferedReader(new FileReader(new File("./input/"+inputFile)));

            String[] header = br.readLine().split(" ");
            Si = Integer.parseInt(header[0]);
            Smax = Integer.parseInt(header[1]);
            T = Integer.parseInt(header[2]);
            D = Integer.parseInt(header[3]);
            Sconsumed = new int[D];
            Twait = new int[D];
            Srecovered = new int[D];
            Nfragment = new int[D];

            String row;
            int i=0;
            while ((row = br.readLine()) != null){
                String[] values = row.split(" ");
                Sconsumed[i] = Integer.parseInt(values[0]);
                Twait[i] = Integer.parseInt(values[1]);
                Srecovered[i] = Integer.parseInt(values[2]);
                Nfragment[i] = Integer.parseInt(values[3]);
                fragments.add(Arrays.asList(values).subList(4, values.length)
                        .stream().map(Integer::parseInt)
                        .collect(Collectors.toList()));
                i++;
            }
        } catch (IOException e) { e.printStackTrace(); }
    }
}
