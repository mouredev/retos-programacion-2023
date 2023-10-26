MovingObject objA = new(new(2, 2), new(1, 2));
MovingObject objB = new(new(5, 5), new(0, -1));
CalculateMeetingPoint(objA, objB);

void CalculateMeetingPoint(MovingObject objA, MovingObject objB)
{

    var tx = (objA.Position.X - objB.Position.X) / (objB.SpeedVector.X - objA.SpeedVector.X);
    var ty = (objA.Position.Y - objB.Position.Y) / (objB.SpeedVector.Y - objA.SpeedVector.Y);

    if (tx != ty)
    {
        Console.WriteLine("The objects are not located anywhere on the plane");
    }
    else
    {
        var t = tx;
        Coord CutPoint = new(objA.Position.X + t * objA.SpeedVector.X, objA.Position.Y + t * objA.SpeedVector.Y);
        Console.WriteLine($"The objects have been found at point {CutPoint} after {t} seconds");
    }
}

class MovingObject
{
    public Coord Position { get; set; }
    public Coord SpeedVector { get; set; }

    public MovingObject(Coord position, Coord speedVector)
    {
        Position = position;
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