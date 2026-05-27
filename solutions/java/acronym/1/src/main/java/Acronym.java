class Acronym {

    private String phrase;

    Acronym(String phrase) {
        this.phrase = phrase;
    }

    String get() {
        String[] words = phrase.split("[\\s-_]+");
        String acronym = "";
        for (String word : words) {
            word = word.strip().toUpperCase();
            if (word.length() > 0) {
                acronym += word.charAt(0);
            }
        }
        return acronym;
    }

}
