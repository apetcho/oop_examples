#include<iostream>

/* Shape abstract interface */
class Shape {
public:
    virtual void draw() = 0;
    virtual void moveto(int x, int y) = 0;
    virtual ~Shape(){};
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
    virtual ~Rectangle(){
        std::cout << "[C++] Destroying" << std::endl;
        std::cout << "<rectangle llx=" << this->x << " lly=" << this->y
            << " width="<< this->width
            << " height=" << this->height << ">" << std::endl;
        std::cout << "[C++] Done!" << std::endl;
    }
};

// ***
Rectangle::Rectangle(int x, int y, int w, int h){
    std::cout << "[C++] Creating new rectangle" << std::endl;
    this->x = x;
    this->y = y;
    this->width = w;
    this->height = h;
    std::cout << "<rectangle llx=" << x << " lly=" << y
        << " width=" << width << " height=" << height << ">"
        << std::endl;
    std::cout << "[C++] Done!" << std::endl;
}

// **
void Rectangle::draw(){
    std::cout << "[C++] Drawing" << std::endl
        << " <rectangle llx=" << x << " lly=" << y
        << " width=" << width << " height=" << height << ">"
        << std::endl;
    std::cout << "[C++] Done!" << std::endl;
}

// ***
void Rectangle::moveto(int x, int y){
    std::cout << "[C++] Moving" << std::endl;
    std::cout << "<rectangle llx=" << this->x << " lly=" << this->y
        << " width="<< this->width << " height=" << this->height
        << ">" << std::endl;
    this->x = x;
    this->y = y;
    std::cout << "[C++] To" << std::endl;
    std::cout << " <rectangle llx=" << this->x << " lly=" << this->y
        << " width=" << this->width << " height=" << this->height
        << ">" << std::endl;
    std::cout << "[C++] Done!" << std::endl;
}

/** Circle class */
class Circle : public Shape {
private:
    int x, y;
    int radius;

public:
    Circle(int x, int y, int radius);
    virtual void draw();
    virtual void moveto(int x, int y);
    int getx(){ return this->x; }
    int gety(){ return this->y; }
    int get_radius(){ return this->radius; }
    void setx(int x){ this->x = x; }
    void sety(int y){ this->y = y; }
    void set_radius(int radius ){ this->radius = radius; }
    virtual ~Circle(){
        std::cout << "[C++] Destroying" << std::endl;
        std::cout << "<circle cx=" << this->x << " cy=" << this->y
            << " radius=" << this->radius << ">" << std::endl;
        std::cout << "[C++] Done!" << std::endl;
    }
};

// ***
Circle::Circle(int x, int y, int radius){
    std::cout << "[C++] Creating new circle" << std::endl;
    this->x = x;
    this->y = y;
    this->radius = radius;
    std::cout << "<circle cx=" << x << " cy=" << y
        << " radius=" << radius << ">" << std::endl;
    std::cout << "[C++] Done!" << std::endl;
}

// ***
void Circle::draw(){
    std::cout << "[C++] Drawing" << std::endl;
    std::cout << "<circle cx=" << x << " cy=" << y
        <<  " radius" << radius << ">" << std::endl;
    std::cout << "[C++] Done!" << std::endl;
}

// ***
void Circle::moveto(int x, int y){
    std::cout << "[C++] Moving" << std::endl;
    std::cout << "<circle cx=" << this->x << " cy=" << this->y
        << " radius=" << this->radius << ">" << std::endl;
    this->x = x;
    this->y = y;
    std::cout << "[C++] To" << std::endl;
    std::cout << "<circle cx=" << this->x << " cy=" << this->y
        <<  " radius" << this->radius << ">"<< std::endl;
    std::cout << "[C++] Done!" << std::endl;
}

/* A function that uses a Shape polymorphically */
void handle_shape(Shape* shape){
    std::cout << std::endl
        <<"[C++] <-Polymorphism-> handle_shape():: moving to the corner!"
        << std::endl;
    shape->moveto(0, 0);
}


// -------------
//  Main Driver
// -------------
int main(){
    // using shapes polymorphically 
    Shape* shapes[2];
    shapes[0] = new Rectangle(20, 12, 123, 321);
    shapes[1] = new Circle(21, 12, 2022);

    for(int i=0; i < 2; i++){
        shapes[i]->draw();
        handle_shape(shapes[i]);
    }

    // access a specific class function
    Rectangle* rect = new Rectangle(1, 2, 3, 4);
    rect->set_width(5);
    rect->draw();

    delete rect;
    for(auto shape: shapes){
        delete shape;
    }

    return 0;
}
