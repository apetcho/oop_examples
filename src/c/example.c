#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

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

    printf(" C>> Drawing <Rectangle llx=%d lly=%d width=%d height=%d>\n",
        rect->x, rect->y, rect->width, rect->height);
}

// ***
void Rectangle_moveto(struct Shape* object, int x, int y){
    struct Rectangle *rect = (struct Rectangle *)object;
    rect->x = x;
    rect->y = y;

    printf("  C>> Moving <Rectangle llx=%d lly=%d width=%d height=%d>\n",
        rect->x, rect->y, rect->width, rect->height);
}

// **
void Rectangle_set_width(struct Shape* object, int width){
    struct Rectangle *rect = (struct Rectangle*)object;
    rect->width = width;
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
    struct Rectangle* object = (struct Rectangle*)malloc(
        sizeof(struct Rectangle));
    object->super.funTable = (struct ShapeFunTable*)&rectangleFunTable;
    object->x = x;
    object->y = y;
    object->width = width;
    object->height = height;

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
    printf("  C>> Drawing <Circle cx=%d cy=%d radius=%d>\n",
        circle->x, circle->y, circle->radius);
}
