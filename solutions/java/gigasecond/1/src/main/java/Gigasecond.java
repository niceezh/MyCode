import java.time.LocalDate;
import java.time.LocalDateTime;

public class Gigasecond {

    private static final long GIGASECOND = 1000000000L;

    private LocalDateTime moment;

    public Gigasecond(LocalDate moment) {
        LocalDateTime momentTrans = moment.atTime(0, 0);
        this.moment = momentTrans.plusSeconds(GIGASECOND);
    }

    public Gigasecond(LocalDateTime moment) {
        this.moment = moment.plusSeconds(GIGASECOND);
    }

    public LocalDateTime getDateTime() {
        return moment;
    }

}
