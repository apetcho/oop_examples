#include<iostream>

/* Shape abstract interface */
class Shape {
public:
    virtual void draw() = 0;
    virtual void moveto(int x, int y) = 0;
};

/* Rectangle class */
class Rectangle : public Shape {
private:
    int x, y;
    int width;
    int height;

public:
    Rectangle(int x, int y, int w, int h);
    int getx(){ return this->x; }
    int gety(){ return this->y; }
    int get_width(){ return this->width; }
    int get_height(){ return this->height; }
    void setx(int x){ this->x = x; }
    void sety(int y){ this->y = y; }
    void set_width(int w){ this->width = w; }
    void set_height(int h){ this->height = h; }
    virtual void draw();
    virtual void moveto(int x, int y);
};

// ***
Rectangle::Rectangle(int x, int y, int w, int h){
    this->x = x;
    this->y = y;
    this->width = w;
    this->height = h;
}

// **
void Rectangle::draw(){
    std::cout << "Rectangle with WIDTH = " << width
        << ", HEIGHT = " << height
        << " at position (" << x << ", " << y << ")"
        << std::endl;
}
