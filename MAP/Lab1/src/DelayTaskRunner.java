import java.util.Random;

public class DelayTaskRunner extends TaskRunnerDecorator{
    DelayTaskRunner(TaskRunner _tsk) {
        super(_tsk);
    }

    @Override
    public void executeAll() {
        Random r = new Random();
        try {
            Integer time = r.nextInt(100) * 10;
            Thread.sleep(time);
            System.out.println("Time = " + time);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        super.executeAll();
    }


}
