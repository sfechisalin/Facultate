public abstract class TaskRunnerDecorator implements TaskRunner{
    private TaskRunner _tskR;

    TaskRunnerDecorator(TaskRunner _tskR){
        this._tskR = _tskR;
    }

    @Override
    public void executeOneTask() {
        _tskR.executeOneTask();
    }

    @Override
    public void executeAll() {
        _tskR.executeAll();
    }

    @Override
    public void addTask(Task t) {
        _tskR.addTask(t);
    }

    @Override
    public boolean hasTask() {
        return _tskR.hasTask();
    }
}
