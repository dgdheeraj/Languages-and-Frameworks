class Bike {
    public int gear;
    public int speed;

    public Bike(int gear, int speed)
    {
        this.speed  = speed;
        this.gear = gear;
    }

    public void applyBrake(int decrement)
    {
        this.speed -= decrement;
    }
    public void speedUp(int increment)
    {
        this.speed += increment;
    }
    public String toString()
    {
        return "Num Gears: " + this.gear + " Speed: " + this.speed ;
    }
}

class MountainBike extends Bike {
    public int seatHeight;

    public MountainBike(int gear,int speed, int seatHeight)
    {
        super(gear, speed);
        this.seatHeight = seatHeight;
    }

    public void setHeight(int height)
    {
        this.seatHeight = height;
    }

    @Override
    public String toString()
    {
        return "Num Gears: " + this.gear + " Speed: " + this.speed + " Seat Height: " + this.seatHeight;
    }
}

public class TestInheritance {
    public static void main(String args[])
    {
        Bike obj1 = new MountainBike(5, 10, 8);
        System.out.println(obj1.toString());
        System.out.println(obj1.getClass());
    }
}