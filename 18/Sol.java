import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

class Scratch {

    private record Pair(long y, long x) {
        Pair addMultiple(Pair other, long multiple) {
            return new Pair(y + other.y * multiple, x + other.x * multiple);
        }

        Pair copy() {
            return new Pair(y, x);
        }

        @Override
        public int hashCode() {
//            return Objects.hash(x, y);
            return (int)x * 31 + (int)y;
        }
    }

    private static Map<Character, Pair> dirs = Map.of(
            '0', new Pair(0, 1),
            '1', new Pair(1, 0),
            '2', new Pair(0, -1),
            '3', new Pair(-1, 0)
    );

    private static long area(List<Pair> points) {
        long area = 0;
        int j;
        for (int i = 0; i < points.size(); i++) {
            j = (i + 1) % points.size();
            area += points.get(i).x * points.get(j).y - points.get(j).x * points.get(i).y;
        }
        return area / 2;
    }

    public static void main(String[] args) throws IOException {
        var lines = Files.readAllLines(Path.of("C:\\Users\\phase\\PycharmProjects\\aoc2023\\18\\input.txt"));
        var pos = new Pair(0, 0);

        long start = System.currentTimeMillis();
        var vertices = new HashSet<Pair>(200000000, 0.75f); // resizing costs 2 seconds
        var points = new ArrayList<Pair>();


        for (String line : lines) {
            String[] parse = line.split(" ");
            Pair dir = dirs.get(parse[2].charAt(parse[2].length() - 2));
            long amount = Long.parseLong(parse[2].substring(2, 7), 16);
            for (long i = 0; i < amount; i++) {
                vertices.add(pos.addMultiple(dir, i));
            }
            pos = pos.addMultiple(dir, amount);
            points.add(pos.copy());
        }

        long area = area(points);
        long b = vertices.size();
        long b2 = b / 2;
        long a1 = area + 1;
        long a2 = a1 - b2;
        long ans = a2 + b;
        System.out.println("Time s: " + (System.currentTimeMillis() - start) / 1000f);
        System.out.println("Ans: " + ans);
    }
}