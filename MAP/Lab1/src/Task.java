public abstract class Task {
    private int taskId;
    private String descriere;

    Task(){

    }

    Task(int taskId, String descriere) {
        this.taskId = taskId;
        this.descriere = descriere;
    }

    public int getTaskId() {
        return taskId;
    }

    public void setTaskId(int taskId) {
        this.taskId = taskId;
    }

    public String getDescriere() {
        return descriere;
    }

    public void setDescriere(String descriere) {
        this.descriere = descriere;
    }

    @Override
    public String toString() {
        return "Task{" +
                "taskId=" + taskId +
                ", descriere='" + descriere + '\'' +
                '}';
    }
    public abstract void execute();

}