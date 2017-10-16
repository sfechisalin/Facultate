public class Main {
    public static void main(String[] args)
    {
      System.out.println();
      System.out.println("Executing via StrategyTaskRunner. :) \n");
      StrategyTaskRunner _str;
      if (args[0].equals("StackContainer"))
         _str = new StrategyTaskRunner(Strategy.StackContainer);
      else
         _str = new StrategyTaskRunner(Strategy.QueueContainer);
        _str.addTask(new MessageTask(1, "Clean Desktop", "desktop"));
        _str.addTask(new MessageTask(2, "Install IntelIJ", "instalare program"));
        _str.addTask(new MessageTask(3,"start codding", "code"));

        _str.executeAll();

        System.out.println("Executing via PrinterTaskRunner. :) \n");
        PrinterTaskRunner _ptr;
        if (args[0].equals("StackContainer"))
            _ptr = new PrinterTaskRunner(new StrategyTaskRunner(Strategy.StackContainer));
        else
            _ptr = new PrinterTaskRunner(new StrategyTaskRunner(Strategy.QueueContainer));

        _ptr.addTask(new MessageTask(1, "Clean Desktop", "desktop"));
        _ptr.addTask(new MessageTask(2, "Install IntelIJ", "instalare program"));
        _ptr.addTask(new MessageTask(3,"start codding", "code"));

        _ptr.executeAll();

        System.out.println("Executing via DelayTaskRunner. :) \n");
        DelayTaskRunner _dtr;

        if (args[0].equals("StackContainer"))
            _dtr = new DelayTaskRunner(new StrategyTaskRunner(Strategy.StackContainer));
        else
            _dtr = new DelayTaskRunner(new StrategyTaskRunner(Strategy.QueueContainer));

        _dtr.addTask(new MessageTask(1, "Clean Desktop", "desktop"));
        _dtr.addTask(new MessageTask(2, "Install IntelIJ", "instalare program"));
        _dtr.addTask(new MessageTask(3,"start codding", "code"));

        _dtr.executeAll();

    }
}
