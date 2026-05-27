import java.util.Arrays;

class ResistorColor {

    private String[] colors = new String[]{"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};

    int colorCode(String color) {
        return Arrays.asList(colors).indexOf(color);
    }

    String[] colors() {
        return colors;
    }

}
