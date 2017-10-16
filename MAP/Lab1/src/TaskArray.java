import java.util.Vector;

public class TaskArray {
    Vector<Task> v;

    TaskArray(){
        v = new Vector<Task>();
    }

    public Task get(int pos){
        assert  pos >= 1 && pos < v.size();
        return v.get(pos - 1);
    }

    public void add(Task elem){
        v.addElement(elem);
    }

    public void add(int index, Task elem) {
        v.add(index, elem);
    }

    public void delete(int pos){
        assert pos >= 1 && pos < v.size();
        v.remove(pos - 1);
    }

    public int size(){
        return v.size();
    }
}
