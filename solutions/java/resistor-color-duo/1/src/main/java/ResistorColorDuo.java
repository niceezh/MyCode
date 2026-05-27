import java.util.Arrays;
import java.util.List;

class ResistorColorDuo {

    private List<String> colorTable = Arrays.asList("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white");

    int value(String[] colors) {
        return colorTable.indexOf(colors[0]) * 10 + colorTable.indexOf(colors[1]);
    }

}
