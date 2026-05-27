class RnaTranscription {

    String transcribe(String dnaStrand) {
        String rnaStrand = "";
        for (int i = 0; i < dnaStrand.length(); i++) {
            char c = dnaStrand.charAt(i);
            if (c == 'G') {
                rnaStrand += 'C';
                continue;
            }
            if (c == 'C') {
                rnaStrand += 'G';
                continue;
            }
            if (c == 'T') {
                rnaStrand += 'A';
                continue;
            }
            if (c == 'A') {
                rnaStrand += 'U';
                continue;
            }
            throw new IllegalArgumentException("Invalid input");
        }
        return rnaStrand;
    }

}
