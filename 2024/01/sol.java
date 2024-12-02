import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.stream.Collectors;

class Scratch {
    public static void main(String[] args) throws IOException {
        var listA = new ArrayList<Integer>();
        var listB = new ArrayList<Integer>();
        Files.lines(Path.of("C:\\Users\\phase\\PycharmProjects\\aoc\\2024\\01\\input"))
                .map(line -> line.split("\\s+"))
                .forEach(line -> {
                    listA.add(Integer.valueOf(line[0]));
                    listB.add(Integer.valueOf(line[1]));
                });
        listA.sort(Integer::compareTo);
        listB.sort(Integer::compareTo);

        var part1 = 0;
        for (int i = 0; i < listA.size(); i++) {
            part1 += Math.abs(listA.get(i) - listB.get(i));
        }
        System.out.println(part1);

        var bFreq = listB.stream().collect(Collectors.groupingBy(i -> i, Collectors.counting()));
        var part2 = 0;
        for (int ai : listA) {
            part2 += ai * bFreq.getOrDefault(ai, 0L).intValue();
        }
        System.out.println(part2);

    }

}