interface Shape {
    abstract public double area();
    abstract public String toString();
}

class Circle implements Shape {
    double radius;
    String color;

    public Circle(String color, double radius)
    {
        this.color = color;
        this.radius = radius;
        System.out.println("Circle Constructor called");
    }

    public double area()
    {
        return Math.PI* Math.pow(radius, 2);
    }

    public String toString()
    {
        return "Circle color: " + this.color + " Area is: " + area();
    }

}

class Rectangle implements Shape {
    double length;
    double breadth;
    String color;

    public Rectangle(String color, double length, double breadth)
    {
        this.color = color;
        this.length = length;
        this.breadth = breadth;
    }

    public double area()
    {
        return length*breadth;
    }

    public String toString()
    {
        return "Rect color: " + this.color + " Area is: " + area();
    }
}

public class TestInterface{
    public static void main(String args[])
    {
        Circle obj1 = new Circle("Red", 4);
        Rectangle obj2 = new Rectangle("Blue", 5, 6);
        
        System.out.println(obj1.toString());
        System.out.println(obj2.toString());
    }
}