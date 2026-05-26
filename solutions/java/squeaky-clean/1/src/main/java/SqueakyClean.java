class SqueakyClean {

    static String clean(String identifier) {
        identifier = identifier.replace("0", "o").replace("1", "l").replace("3", "e").replace("4", "a").replace("7", "t");
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < identifier.length(); i++) {
            char c = identifier.charAt(i);
            if (Character.isLetter(c)) {
                builder.append(c);
                continue;
            }
            if (c == ' ') {
                builder.append('_');
                continue;
            }
            if (c == '-') {
                i++;
                if (i < identifier.length()) {
                    builder.append(Character.toUpperCase(identifier.charAt(i)));
                }
            }
        }
        return builder.toString();
    }

}
