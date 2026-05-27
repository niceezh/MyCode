import java.util.Arrays;
import java.util.List;

class ResistorColorTrio {

    private List<String> colorTable = Arrays.asList("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white");

    String label(String[] colors) {
        long value = colorTable.indexOf(colors[0]) * 10 + colorTable.indexOf(colors[1]);
        for (int i = 0; i < colorTable.indexOf(colors[2]); i++) {
            value *= 10;
        }
        String unit;
        if (value < 1000) {
            unit = "ohms";
        } else if (value < 1000000) {
            value /= 1000;
            unit = "kiloohms";
        } else if (value < 1000000000) {
            value /= 1000000;
            unit = "megaohms";
        } else {
            value /= 1000000000;
            unit = "gigaohms";
        }
        return String.format("%d %s", value, unit);
    }

}
