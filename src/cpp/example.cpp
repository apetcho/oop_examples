#include<iostream>

/* Shape abstract interface */
class Shape {
public:
    virtual void draw() = 0;
    virtual void moveto(int x, int y) = 0;
};
