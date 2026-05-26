public class CarsAssemble {

    public static final double PRODUCTION_RATE_PER_HOUR = 221.0;

    public double productionRatePerHour(int speed) {
        switch (speed) {
            case 0, 1, 2, 3, 4:
                return speed * PRODUCTION_RATE_PER_HOUR;
            case 5, 6, 7, 8:
                return speed * PRODUCTION_RATE_PER_HOUR * 0.9;
            case 9:
                return speed * PRODUCTION_RATE_PER_HOUR * 0.8;
            case 10:
                return speed * PRODUCTION_RATE_PER_HOUR * 0.77;
            default:
                throw new IllegalArgumentException("Invalid speed: " + speed);
        }
    }

    public int workingItemsPerMinute(int speed) {
        return (int) (productionRatePerHour(speed) / 60);
    }

}
