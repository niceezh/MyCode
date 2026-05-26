class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar> {

    private int distance;

    private int victory;

    @Override
    public void drive() {
        distance += 10;
    }

    @Override
    public int getDistanceTravelled() {
        return distance;
    }

    public int getNumberOfVictories() {
        return victory;
    }

    public void setNumberOfVictories(int numberOfVictories) {
        victory = numberOfVictories;
    }

    @Override
    public int compareTo(ProductionRemoteControlCar other) {
        return Integer.compare(other.getNumberOfVictories(), this.getNumberOfVictories());
    }

}
