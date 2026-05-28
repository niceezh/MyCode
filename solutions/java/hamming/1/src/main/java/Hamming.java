public class Hamming {

    private String leftStrand;
    private String rightStrand;
    private int lenght;

    public Hamming(String leftStrand, String rightStrand) {
        if (leftStrand.length() != rightStrand.length()) {
            throw new IllegalArgumentException("strands must be of equal length");
        }
        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
        this.lenght = leftStrand.length();
    }

    public int getHammingDistance() {
        int distance = 0;
        for (int i = 0; i < lenght; i++) {
            if (leftStrand.charAt(i) != rightStrand.charAt(i)) {
                distance++;
            }
        }
        return distance;
    }

}
