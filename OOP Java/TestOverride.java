class Parent {
    void Print()
    {
        System.out.println("Inside parent class");
    }
}

class Child1 extends Parent {
    void Print()
    {
        System.out.println("Inside Child1 class");
    }
}

class Child2 extends Parent {
    void Print()
    {
        System.out.println("Inside Child2 class");
    }
}

class TestOverride {
    public static void main(String args[])
    {
        Parent obj = new Parent();
        obj.Print();

        obj = new Child1();
        obj.Print();

        obj = new Child2();
        obj.Print();
    }
}