import java.util.Arrays;

class SortingTak extends Task{
    private int v[];
    SortingTak(int x[]){
        v = new int[x.length];
       System.arraycopy(x,0,x,0,x.length);
       Arrays.sort(v);
    }

    public void execute()
    {
        for (int e : v)
            System.out.print(e + " ");
        System.out.println();
    }
}
