// Test cases

MovingObject obj1A = new(new(2, 2), new(1, 2));
MovingObject obj1B = new(new(5, 5), new(-2, -1));

MovingObject obj2A = new(new(0, 0), new(2, 1));
MovingObject obj2B = new(new(0, 6), new(2, -2));

MovingObject obj3A = new(new(5, 0), new(0, 3));
MovingObject obj3B = new(new(14, 15), new(-3, -2));

MovingObject obj4A = new(new(5, 0), new(0, 3));
MovingObject obj4B = new(new(14, 15), new(3, 2));

CalculateMeetingPoint(obj1A, obj1B);
CalculateMeetingPoint(obj2A, obj2B);
CalculateMeetingPoint(obj3A, obj3B);
CalculateMeetingPoint(obj4A, obj4B);

void CalculateMeetingPoint(MovingObject objA, MovingObject objB)
{

    var dx = objB.Position.X - objA.Position.X;
    var dy = objB.Position.Y - objA.Position.Y;
    var dsx = objB.SpeedVector.X - objA.SpeedVector.X;
    var dsy = objB.SpeedVector.Y - objA.SpeedVector.Y;

    var t = - (dx * dsx + dy * dsy) / (Math.Pow(dsx, 2) + Math.Pow(dsy, 2));

    if (t < 0 || Convert.ToDecimal(t) % 1 != 0)
    {
        Console.WriteLine("Objects do not intersect at any point in the plane");
    }
    else
    {
        Coord CutPoint = new(objA.Position.X + Convert.ToInt32(t) * objA.SpeedVector.X,
            objA.Position.Y + Convert.ToInt32(t) * objA.SpeedVector.Y);
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