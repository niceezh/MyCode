class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter {

    public String toString() {
        return "Fighter is a Warrior";
    }

    @Override
    public boolean isVulnerable() {
        return false;
    }

    @Override
    public int getDamagePoints(Fighter fighter) {
        return fighter.isVulnerable() ? 10 : 6;
    }

}

class Wizard extends Fighter {

    private boolean prepared = false;

    public String toString() {
        return "Fighter is a Wizard";
    }

    public void prepareSpell() {
        prepared = true;
    }

    @Override
    public boolean isVulnerable() {
        return prepared ? false : true;
    }

    @Override
    public int getDamagePoints(Fighter fighter) {
        if (prepared) {
            prepared = false;
            return 12;
        }
        return 3;
    }

}
