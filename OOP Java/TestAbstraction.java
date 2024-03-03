abstract class Shape {
    String color;
    abstract double area();
    public abstract String toString();
    
    public Shape(String color)
    {
        this.color = color;
    }

    String getColor()
    {
        return this.color;
    }
}

class Circle extends Shape {
    double radius;

    public Circle(String color, double radius)
    {
        super(color);
        this.radius = radius;
        System.out.println("Circle Constructor called");
    }

    @Override
    double area()
    {
        return Math.PI* Math.pow(radius, 2);
    }

    @Override
    public String toString()
    {
        return "Circle color: " + super.getColor() + " Area is: " + area();
    }

}

class Rectangle extends Shape {
    double length;
    double breadth;

    public Rectangle(String color, double length, double breadth)
    {
        super(color);
        this.length = length;
        this.breadth = breadth;
    }

    @Override
    double area()
    {
        return length*breadth;
    }

    @Override
    public String toString()
    {
        return "Rect color: " + super.getColor() + " Area is: " + area();
    }
}

public class TestAbstraction{
    public static void main(String args[])
    {
        Circle obj1 = new Circle("Red", 4);
        Rectangle obj2 = new Rectangle("Blue", 5, 6);
        
        System.out.println(obj1.toString());
        System.out.println(obj2.toString());
    }
}