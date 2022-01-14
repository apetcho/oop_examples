#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

#define PRINT_RECT(rect)                                        \
    printf("<rectangle llx=%d lly=%d width=%d height=%d>\n",    \
        rect->x, rect->y, rect->width, rect->height)

#define PRINT_CIRCLE(circle)                    \
    printf("<circle cx=%d cy=%d radius=%d>",     \
        circle->x, circle->y, circle->radius)
/* Shape abstract interface */
struct Shape {
    struct ShapeFunTable *funTable;
};

struct ShapeFunTable {
    void (*draw)(struct Shape* object);
    void (*moveto)(struct Shape* object, int x, int y);
    void (*destroy)(struct Shape *object);
};

// never create an instance shape directly: these make it an abstract interface
struct Shape* Shape_new(){ assert(0); }
void Shape_destroy(struct Shape* object){}

/* Rectangle class */
struct Rectangle {
    struct Shape super;
    int x, y;
    int width;
    int height;
};

// ***
void Rectangle_draw(struct Shape* object){
    struct Rectangle *rect = (struct Rectangle*)object;
    puts("[C] Drawing");
    PRINT_RECT(rect);
    puts("[C] Done!");
}

// ***
void Rectangle_moveto(struct Shape* object, int x, int y){
    struct Rectangle *rect = (struct Rectangle *)object;
    puts("[C] Moving ");
    PRINT_RECT(rect);
    rect->x = x;
    rect->y = y;
    puts("[C] To");
    PRINT_RECT(rect);
    puts("[C] Done!");
}

// **
void Rectangle_set_width(struct Shape* object, int width){
    struct Rectangle *rect = (struct Rectangle*)object;
    puts("[C] Rectangle:: modifiy the width");
    PRINT_RECT(rect);
    rect->width = width;
    puts("[C] Rectangle:: width modified");
    PRINT_RECT(rect);
    puts("[C] Done!");
}

// ***
void Rectangle_destroy(struct Shape *object){
    Shape_destroy(object);
    free(object);
}


// ***
struct RectangleFunTable{
    struct ShapeFunTable super;
    void (*set_width)(struct Shape* object, int width);
} rectangleFunTable = {
    .super = {
        .draw = Rectangle_draw,
        .moveto = Rectangle_moveto,
        .destroy = Rectangle_destroy,
    },
    .set_width = Rectangle_set_width,
};

// ***
struct Shape* Rectangle_new(int x, int y, int width, int height){
    puts("[C] Creating a new rectangle");
    struct Rectangle* object = (struct Rectangle*)malloc(
        sizeof(struct Rectangle));
    object->super.funTable = (struct ShapeFunTable*)&rectangleFunTable;
    object->x = x;
    object->y = y;
    object->width = width;
    object->height = height;
    PRINT_RECT(object);
    puts("[C] Done!");

    return (struct Shape*)object;
}


/** Circle class */
struct Circle{
    struct Shape super;
    int x, y;
    int radius;
};

// ***
void Circle_draw(struct Shape* object){
    struct Circle* circle = (struct Circle*) object;
    puts("[C] Drawing");
    PRINT_CIRCLE(circle);
    puts("[C] Done!");
}

// ***
void Circle_moveto(struct Shape* object, int x, int y){
    struct Circle* circle = (struct Circle*)object;
    puts("[C] Moving ");
    PRINT_CIRCLE(circle);
    puts("[C] To");
    circle->x = x;
    circle->y = y;
    PRINT_CIRCLE(circle);
    puts("[C] Done!");
}
