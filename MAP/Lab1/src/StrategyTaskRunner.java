class StrategyTaskRunner implements TaskRunner{
    Container _c;

    StrategyTaskRunner(Strategy _st)
    {
        if (_st == Strategy.StackContainer)
            _c = TaskContainerFactory.getInstance().createContainer(Strategy.StackContainer);
        else
            _c = TaskContainerFactory.getInstance().createContainer(Strategy.QueueContainer);
    }

    @Override
    public void executeOneTask() {
        if (_c.size() != 0)
            _c.remove().execute();
    }

    @Override
    public void executeAll() {
        for(; _c.size() != 0;)
            _c.remove().execute();
    }

    @Override
    public void addTask(Task t) {
        _c.add(t);
    }

    @Override
    public boolean hasTask() {
        return _c.size() != 0;
    }
}
