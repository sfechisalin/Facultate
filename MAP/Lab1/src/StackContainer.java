public class StackContainer implements Container{
   TaskArray tA;

    StackContainer(){
        tA = new TaskArray();
    }

    @Override
     public Task remove() {
        if (this.isEmpty())
            return null;
        Task _t = tA.get(tA.size());
        tA.delete(tA.size());
        return _t;
     }

     @Override
     public void add(Task task) {
        tA.add(task);
     }

     @Override
     public int size() {
         return tA.size();
     }

     @Override
     public boolean isEmpty() {
         return tA.size() == 0;
     }
 }
