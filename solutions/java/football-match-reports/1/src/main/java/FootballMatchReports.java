import java.util.HashMap;
import java.util.Map;

public class FootballMatchReports {

    public static String onField(int shirtNum) {
        Map<Integer, String> players = new HashMap<>();
        players.put(1, "goalie");
        players.put(2, "left back");
        players.put(3, "center back");
        players.put(4, "center back");
        players.put(5, "right back");
        players.put(6, "midfielder");
        players.put(7, "midfielder");
        players.put(8, "midfielder");
        players.put(9, "left wing");
        players.put(10, "striker");
        players.put(11, "right wing");
        return players.getOrDefault(shirtNum, "invalid");
    }

}
