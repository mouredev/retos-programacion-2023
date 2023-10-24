MovingObject objA = new(new(2, 2), new(1, 2));
MovingObject objB = new(new(5, 5), new(0, -1));

CalculateMeetingPoint(objA, objB);
void CalculateMeetingPoint(MovingObject objA, MovingObject objB)
{
    if (objA.SpeedVector.X / objB.SpeedVector.X == objA.SpeedVector.Y / objB.SpeedVector.Y)
    {
        Console.WriteLine("The objects are not located anywhere on the plane");
        return;
    }
    else
    {
        int seconds = 0;
        while (objA.PointPosition.X != objB.PointPosition.X && objA.PointPosition.Y != objB.PointPosition.Y)
        {
            seconds++;

            objA.PointPosition.X += objA.SpeedVector.X;
            objA.PointPosition.Y += objA.SpeedVector.Y;
            objB.PointPosition.X += objB.SpeedVector.X;
            objB.PointPosition.Y += objB.SpeedVector.Y;
        }

        Console.WriteLine($"The objects have been found at point {objA.PointPosition.ToString()} after {seconds} seconds");
    }
}

class MovingObject
{
    public Coord PointPosition { get; set; }
    public Coord SpeedVector { get; set; }

    public MovingObject(Coord pointPosition, Coord speedVector)
    {
        PointPosition = pointPosition;
        SpeedVector = speedVector;
    }
}

class Coord
{
    public int X { get; set; }
    public int Y { get; set; }

    public Coord(int x, int y)
    {
        X = x;
        Y = y;
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }
}