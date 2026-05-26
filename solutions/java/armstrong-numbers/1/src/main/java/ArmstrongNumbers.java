class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {
        int number = numberToCheck;
        int numberOfDigits = String.valueOf(number).length();
        int sum = 0;
        while (number != 0) {
            int digit = number % 10;
            sum += Math.pow(digit, numberOfDigits);
            number /= 10;
        }
        return numberToCheck == sum;
    }

}
