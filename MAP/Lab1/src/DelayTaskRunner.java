public class DelayTaskRunner extends TaskRunnerDecorator{
    DelayTaskRunner(TaskRunner _tsk) {
        super(_tsk);
    }

    @Override
    public void executeOneTask() {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        super.executeOneTask();
    }

    @Override
    public void executeAll() {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        super.executeAll();
    }

    @Override
    public void addTask(Task t) {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        super.addTask(t);
    }

    @Override
    public boolean hasTask() {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return super.hasTask();
    }
}
