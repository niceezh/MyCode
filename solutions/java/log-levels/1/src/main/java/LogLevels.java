import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LogLevels {

    public static String message(String logLine) {
        Pattern pattern = Pattern.compile(":(.*)");
        Matcher matcher = pattern.matcher(logLine);
        return matcher.find() ? matcher.group(1).trim() : "";
    }

    public static String logLevel(String logLine) {
        Pattern pattern = Pattern.compile("\\[(.*)\\]");
        Matcher matcher = pattern.matcher(logLine);
        return matcher.find() ? matcher.group(1).trim().toLowerCase() : "";
    }

    public static String reformat(String logLine) {
        return String.format("%s (%s)", message(logLine), logLevel(logLine));
    }

}
