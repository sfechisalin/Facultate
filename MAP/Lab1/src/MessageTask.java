public class MessageTask extends Task {
    String message;
    MessageTask(int _taskId, String _description, String _message){
        super(_taskId, _description);
        message = _message;
    }

    @Override
    public void execute(){
        System.out.println(message);
    }
}
