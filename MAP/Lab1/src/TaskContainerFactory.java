public class TaskContainerFactory implements IFactory {

    private static TaskContainerFactory ourInstance = new TaskContainerFactory();;
    private TaskContainerFactory() {
    }

    @Override
    public Container createContainer(Strategy _st) {
        if (_st == Strategy.StackContainer)
            return new StackContainer();
        return new QueueContainer();
    }

    public static TaskContainerFactory getInstance() {
        return ourInstance;
    }
}
