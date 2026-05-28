class MicroBlog {

    public String truncate(String input) {
        String str = "";
        int count = 0;
        for (int i = 0; i < input.length(); ) {
            int cp = input.codePointAt(i);
            str += Character.toString(cp);
            count++;
            if (count == 5) {
                break;
            }
            i += Character.charCount(cp);
        }
        return str;
    }

}
