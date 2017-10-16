import java.time.LocalDateTime;

public class PrinterTaskRunner extends TaskRunnerDecorator{
    PrinterTaskRunner(TaskRunner _tsk) {
        super(_tsk);
    }
    @Override
    public void executeOneTask() {
        super.executeOneTask();
        System.out.println(LocalDateTime.now().getHour() + ":" + LocalDateTime.now().getMinute() + ":" + LocalDateTime.now().getSecond());
    }

    @Override
    public void executeAll() {
        super.executeAll();
        System.out.println(LocalDateTime.now().getHour() + ":" + LocalDateTime.now().getMinute() + ":" + LocalDateTime.now().getSecond());
    }

    @Override
    public void addTask(Task t) {
        super.addTask(t);
        System.out.println(LocalDateTime.now().getHour() + ":" + LocalDateTime.now().getMinute() + ":" + LocalDateTime.now().getSecond());
    }

    @Override
    public boolean hasTask() {
        System.out.println(LocalDateTime.now().getHour() + ":" + LocalDateTime.now().getMinute() + ":" + LocalDateTime.now().getSecond());
        return super.hasTask();

    }
}
