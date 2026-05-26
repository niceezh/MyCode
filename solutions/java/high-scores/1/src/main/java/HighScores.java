import java.util.ArrayList;
import java.util.List;

class HighScores {

    private List<Integer> scores = new ArrayList<>();

    public HighScores(List<Integer> highScores) {
        this.scores = highScores;
    }

    List<Integer> scores() {
        return scores;
    }

    Integer latest() {
        return scores.get(scores.size() - 1);
    }

    Integer personalBest() {
        return scores.stream().max(Integer::compareTo).get();
    }

    List<Integer> personalTopThree() {
        return scores.stream().sorted((a, b) -> b - a).limit(3).toList();
    }

}
