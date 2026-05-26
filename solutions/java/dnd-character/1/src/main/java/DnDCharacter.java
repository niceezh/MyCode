import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class DnDCharacter {

    private int strength = ability(rollDice());
    private int dexterity = ability(rollDice());
    private int constitution = ability(rollDice());
    private int intelligence = ability(rollDice());
    private int wisdom = ability(rollDice());
    private int charisma = ability(rollDice());

    int ability(List<Integer> scores) {
        List<Integer> scoresCopy = new ArrayList<>(scores);
        scoresCopy.sort(null);
        return scoresCopy.get(1) + scoresCopy.get(2) + scoresCopy.get(3);
    }

    List<Integer> rollDice() {
        Random random = new Random();
        List<Integer> dice = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            dice.add(random.nextInt(6) + 1);
        }
        return dice;
    }

    int modifier(int input) {
        return Math.floorDiv(input - 10, 2);
    }

    int getStrength() {
        return strength;
    }

    int getDexterity() {
        return dexterity;
    }

    int getConstitution() {
        return constitution;
    }

    int getIntelligence() {
        return intelligence;
    }

    int getWisdom() {
        return wisdom;
    }

    int getCharisma() {
        return charisma;
    }

    int getHitpoints() {
        return 10 + modifier(constitution);
    }

}
