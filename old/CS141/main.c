#include <malloc.h>
#include <stdio.h>
#include <string.h>

typedef double (*VirtualMethodPointer)(void *);
typedef VirtualMethodPointer * VTableType;
typedef struct Shape Shape;
typedef struct Triangle Triangle;
typedef struct Square Square;
typedef struct Rectangle Rectangle;
typedef struct Circle Circle;

#define PI 3.14159

struct Shape
{
  VTableType VPointer;
  char *name;
};

double Shape_area(Shape *_this)
{
  return 0.0;
}

void Shape_draw(Shape *_this)
{
}

VirtualMethodPointer Shape_VTable [] =
{
  (VirtualMethodPointer)Shape_area,
  (VirtualMethodPointer)Shape_draw
};

Shape * Shape_Shape(Shape * _this, char *newName)
{
  _this->VPointer = Shape_VTable;
  _this->name = newName;
  return _this;
}

struct Triangle
{
  VTableType VPointer;
  char *name;
  double base;
  double height;
};

double Triangle_area(Triangle *_this)
{
  return (1.0/2.0) * (_this->base * _this->height);
}

void Triangle_draw(Triangle *_this)
{
  char drawing[200] = "";
  for (int i = 0; i < _this->height; i++)
  {
    strcpy(drawing, "*");
    for (int j = 0; j < i; j++)
    {
      strcpy(drawing, " *");
    }
    strcpy(drawing, "\n");

  }
  printf("%s: base=%f height=%f\n", _this->name, _this->base, _this->height);
  printf(drawing);
}

VirtualMethodPointer Triangle_VTable [] =
{
  (VirtualMethodPointer)Triangle_area,
  (VirtualMethodPointer)Triangle_draw
};

Triangle * Triangle_Triangle(Triangle * _this, char *newName, double newBase, double newHeight)
{
  Shape_Shape((Shape *)_this, newName);
  _this->VPointer = Triangle_VTable;
  _this->base = newBase;
  _this->height = newHeight;
  return _this;
}

struct Square
{
  VTableType VPointer;
  char *name;
  double height;
};

double Square_area(Square *_this)
{
  return _this->height * _this->height;
}

void Square_draw(Square *_this)
{
  char drawing[200] = "";
  for (int i = 0; i < _this->height; i++)
  {
    strcpy(drawing, "*");
    for (int j = 0; j < _this->height - 2; j++)
    {
      if (i == 0 || i == _this->height - 1) {
        strcpy(drawing, "* ");
      }
      else {
        strcpy(drawing, "  ");
      }
    }
    strcpy(drawing, "*\n");
  }
  printf("%s: height=%f\n", _this->name, _this->height);
  printf("%s\n", drawing);
}

VirtualMethodPointer Square_VTable [] =
{
  (VirtualMethodPointer)Square_area,
  (VirtualMethodPointer)Square_draw
};

Square * Square_Square(Square * _this, char *newName, double newHeight)
{
  Shape_Shape((Shape *)_this, newName);
  _this->VPointer = Square_VTable;
  _this->height = newHeight;
  return _this;
}

struct Rectangle
{
  VTableType VPointer;
  char *name;
  double height;
  double width;
};

double Rectangle_area(Rectangle *_this)
{
  return _this->width * _this->height;
}

void Rectangle_draw(Rectangle *_this)
{
  char drawing[200] = "";
  for (int i = 0; i < _this->height; i++)
  {
    strcpy(drawing, "* ");
    for (int j = 0; j < _this->width; j++)
    {
      if (i == 0 || i == _this->height - 1)
      {
        strcpy(drawing, "* ");
      }
      else
      {
        strcpy(drawing, "  ");
      }
    }
  strcpy(drawing, "*\n");
  }
  printf("%s: height=%f width=%f\n", _this->name, _this->height, _this->width);
  printf("%s\n", drawing);
}

VirtualMethodPointer Rectangle_VTable [] =
{
  (VirtualMethodPointer)Rectangle_area,
  (VirtualMethodPointer)Rectangle_draw
};

Rectangle * Rectangle_Rectangle(Rectangle * _this, char *newName, double newWidth, double newHeight)
{
  Square_Square((Square *)_this, newName, newHeight);
  _this->VPointer = Rectangle_VTable;
  _this->width = newWidth;
  return _this;
}

struct Circle
{
  VTableType VPointer;
  char *name;
  double radius;
};

double Circle_area(Circle *_this)
{
  return PI * _this->radius * _this->radius;
}

void Circle_draw(Circle *_this)
{
  char drawing[30000] = "";
  double offset = _this->radius + 1;
  for (int i = -_this->radius; i < _this->radius; i++)
  {
    for (int j = -_this->radius; j < _this->radius; j++)
    {
      if ((i * i + j * j) < _this->radius * _this->radius)
      {
        strcpy(drawing, "* ");
      }
      else
      {
        strcpy(drawing, "  ");
      }
    }
    strcpy(drawing, "\n");
  }
  printf("%s: radius=%f\n", _this->name, _this->radius);
  printf("%s\n", drawing);
}

VirtualMethodPointer Circle_VTable [] =
{
  (VirtualMethodPointer)Circle_area,
  (VirtualMethodPointer)Circle_draw
};

Circle * Circle_Circle(Circle * _this, char *newName, double newRadius)
{
  Shape_Shape((Shape *)_this, newName);
  _this->VPointer = Circle_VTable;
  _this->radius = newRadius;
  return _this;
}

int main()
{
  Shape * s[] = {
    (Shape *)Triangle_Triangle((Triangle *)malloc(sizeof(Triangle)), "FirstTriangle", 5.0, 5.0),
    (Shape *)Triangle_Triangle((Triangle *)malloc(sizeof(Triangle)), "SecondTriangle", 4.0, 3.0),
    (Shape *)Circle_Circle((Circle *)malloc(sizeof(Circle)), "FirstCircle", 5.0),
    (Shape *)Circle_Circle((Circle *)malloc(sizeof(Circle)), "SecondCircle", 10.0),
    (Shape *)Square_Square((Square *)malloc(sizeof(Square)), "FirstSquare", 5.0),
    (Shape *)Square_Square((Square *)malloc(sizeof(Square)), "SecondSquare", 10.0),
    (Square *)Rectangle_Rectangle((Rectangle *)malloc(sizeof(Rectangle)), "FirstRectangle", 4.0, 8.0),
    (Square *)Rectangle_Rectangle((Rectangle *)malloc(sizeof(Rectangle)), "SecondRectangle", 8.0, 4.0)
  };

  int i;
  double totalArea = 0.0;
  for (i = 0; i < sizeof(s) / sizeof(*s); i++)
  {
    printf("Area = %f\n", (s[i]->VPointer[0])(s[i]));
    totalArea += (s[i]->VPointer[0])(s[i]);
    (s[i]->VPointer[1](s[i]));
    free(s[i]);
  }
  printf("Total Area = %f\n", totalArea);

}
