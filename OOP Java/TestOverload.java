class Helper {
    
    static int multiply(int a, int b)
    {
        return a*b;
    }

    static double multiply(double a, double b)
    {
        return a*b;
    }
}

public class TestOverload {
    
    public static void main(String args[])
    {
        System.out.println(Helper.multiply(3,4));
        System.out.println(Helper.multiply(3.5,4.5));
    }
}