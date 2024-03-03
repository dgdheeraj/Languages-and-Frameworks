class Singleton {
    static private Singleton obj;

    private Singleton () {}

    public static Singleton getSingleton() {
        if (obj == null)
        {
            obj = new Singleton();
        }

        return obj;
    }
}

public class TestSingleton {
    public static void main(String args[])
    {
        // Will give error
        //Singleton obj1 = new Singleton();
        
        Singleton obj2 = Singleton.getSingleton();
        Singleton obj3 = Singleton.getSingleton();
        System.out.println(obj2 == obj3);
    }
}