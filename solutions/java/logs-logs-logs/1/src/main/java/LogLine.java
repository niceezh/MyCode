import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LogLine {

    private String logLine;

    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    public LogLevel getLogLevel() {
        Pattern pattern = Pattern.compile("\\[(.*)\\]");
        Matcher matcher = pattern.matcher(logLine);
        String logLevel = "";
        if (matcher.find()) {
            logLevel = matcher.group(1);
        }
        switch (logLevel) {
            case "TRC":
                return LogLevel.TRACE;
            case "DBG":
                return LogLevel.DEBUG;
            case "INF":
                return LogLevel.INFO;
            case "WRN":
                return LogLevel.WARNING;
            case "ERR":
                return LogLevel.ERROR;
            case "FTL":
                return LogLevel.FATAL;
            default:
                return LogLevel.UNKNOWN;
        }
    }

    public String getOutputForShortLog() {
        LogLevel logLevel = getLogLevel();
        int logCode = logLevel.getCode();
        Pattern pattern = Pattern.compile(":(.*)");
        Matcher matcher = pattern.matcher(logLine);
        String message = "";
        if (matcher.find()) {
            message = matcher.group(1).strip();
        }
        return String.format("%d:%s", logCode, message);
    }

}
