import java.util.HashSet;
import java.util.List;
import java.util.Set;

class GottaSnatchEmAll {

    static Set<String> newCollection(List<String> cards) {
        Set<String> collection = new HashSet<>();
        for (String card : cards) {
            collection.add(card);
        }
        return collection;
    }

    static boolean addCard(String card, Set<String> collection) {
        return collection.add(card);
    }

    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        return !myCollection.containsAll(theirCollection) && !theirCollection.containsAll(myCollection);
    }

    static Set<String> commonCards(List<Set<String>> collections) {
        Set<String> commonCards = new HashSet<>();
        for (Set<String> collection : collections) {
            commonCards.addAll(collection);
        }
        for (Set<String> collection : collections) {
            commonCards.retainAll(collection);
        }
        return commonCards;
    }

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> allCards = new HashSet<>();
        for (Set<String> collection : collections) {
            allCards.addAll(collection);
        }
        return allCards;
    }

}
