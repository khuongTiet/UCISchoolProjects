class Shape {
  String name;
  Shape() {
  }
  Shape(String newName)
  {
    name = newName;
  }

  double area() {
    return 0.0;
  }

  void draw()
  {
    System.out.println("Shape.draw() You should never see this");
  }
}

class Triangle extends Shape
{
  int myHeight, myBase;
  Triangle(String name, int h, int b)
  {
    super(name);
    myHeight = h;
    myBase = b;
  }

  double area()
  {
    return (double)((double)(myBase * myHeight) / 2);
  }

  void draw()
  {
    String drawing = "";
    for (int i = 0; i < myHeight; i++)
    {
      drawing += "*";
      for (int j = 0; j < i; j++)
      {
        drawing += " *";
      }
      drawing += "\n";

    }
    System.out.printf("%s: height=%d base=%d\n", name, myHeight, myBase);
    System.out.println(drawing);
  }
}


class Square extends Shape
{
  int myHeight;

  Square(String name, int h)
  {
    super(name);
    myHeight = h;
  }

  double area()
  {
    return Math.pow(myHeight, 2);
  }

  void draw()
  {
    String drawing = "";
    for (int i = 0; i < myHeight; i++)
    {
      drawing += "* ";
      for (int j = 0; j < myHeight - 2; j++)
      {
        if (i == 0 || i == myHeight - 1) {
          drawing += "* ";
        }
        else {
          drawing += "  ";
        }
      }
      drawing += "*\n";
    }
    System.out.printf("%s: height=%d\n", name, myHeight);
    System.out.println(drawing);
  }

}

class Rectangle extends Square
{
  int myWidth;

  Rectangle(String name, int h, int w)
  {
    super(name, h);
    myWidth = w;
  }

  double area()
  {
    return myHeight * myWidth;
  }

  void draw()
  {
    String drawing = "";
    for (int i = 0; i < myHeight; i++)
    {
      drawing += "* ";
      for (int j = 0; j < myWidth; j++)
      {
        if (i == 0 || i == myHeight - 1)
        {
          drawing += "* ";
        }
        else
        {
          drawing += "  ";
        }
      }
      drawing += "*\n";
    }
    System.out.printf("%s: height=%d width=%d\n", name, myHeight, myWidth);
    System.out.println(drawing);
  }
}


class Circle extends Shape
{
  int myRadius;

  Circle(String name, int r)
  {
    super(name);
    myRadius = r;
  }

  double area()
  {
    return (double)(Math.PI * Math.pow(myRadius, 2));
  }

  void draw()
  {
    String drawing = "";
    double offset = myRadius + 1;
    for (int i = -myRadius; i < myRadius; i++)
    {
      for (int j = -myRadius; j < myRadius; j++)
      {
        if ((Math.pow(i, 2) + Math.pow(j, 2)) < Math.pow(myRadius, 2))
        {
          drawing += "* ";
        }
        else
        {
          drawing += "  ";
        }
      }
      drawing += "\n";
    }
    System.out.printf("%s: radius=%d\n", name, myRadius);
    System.out.println(drawing);
  }
}

class Picture
{
  class Node
  {
    Shape value = null;
    Node next = null;
    Node(Shape val, Node nxt)
    {
      value = val; next = nxt;
    }
  }
  Node head;
  Picture() {head = null;}
  void add(Shape sh){head = new Node(sh, head);}
  void drawAll()
  {
    Node current = head;
    while(current != null)
    {
      current.value.draw();
      current = current.next;
    }

  }
  double totalArea()
  {
    Node current = head;
    double area = 0;
    while(current != null)
    {
      area += current.value.area();
      current = current.next;
    }
    return area;
  }
}


public class mainClass {
  public static void main(String[] args) {
    Picture p = new Picture();
    p.add(new Triangle("FirstTriangle", 5, 5));
    p.add(new Triangle("SecondTriangle", 4, 3));
    p.add(new Circle("FirstCircle", 5));
    p.add(new Circle("SecondCircle", 10));
    p.add(new Square("FirstSquare", 5));
    p.add(new Square("SecondSquare", 10));
    p.add(new Rectangle("FirstRectangle", 4, 8));
    p.add(new Rectangle("SecondRectangle", 8, 4));
    p.drawAll();
    System.out.println(p.totalArea());
  }
}
