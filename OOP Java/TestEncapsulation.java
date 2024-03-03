class Person {
    private String name;
    private int age;

    Person(String name, int age)
    {
        this.name = name;
        this.age = age;
    }

    public String getName()
    {
        return this.name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public int getAge()
    {
        return this.age;
    }

    public void setAge(int age)
    {
        this.age = age;
    }

    public String getDetails()
    {
        return "Name: " + this.name + " Age: " + this.age;
    }
}

public class TestEncapsulation {
    public static void main(String args[])
    {
        Person p1 = new Person("ABC", 12);
        System.out.println(p1.getDetails());
        p1.setName("Dheeraj");
        p1.setAge(25);
        System.out.println(p1.getDetails());
    }
}