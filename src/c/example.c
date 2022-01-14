#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

#define PRINT_RECT(rect)                                        \
    printf("<rectangle llx=%d lly=%d width=%d height=%d>\n",    \
        ((rect)->x), ((rect)->y), ((rect)->width), ((rect)->height))

#define PRINT_CIRCLE(circle)                        \
    printf("<circle cx=%d cy=%d radius=%d>\n",      \
        ((circle)->x), ((circle)->y), ((circle)->radius))

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
    puts("[C] Destroying ");
    PRINT_RECT((struct Rectangle*)object);
    Shape_destroy(object);
    free(object);
    puts("[C] Done!");
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

// ***
void Circle_destroy(struct Shape *object){
    puts("[C] Destroying ");
    PRINT_CIRCLE((struct Circle*)object);
    Shape_destroy(object);
    free(object);
    puts("[C] Done!");
}

// ***
struct CircleFunTable{
    struct ShapeFunTable super;
} circleFunTable = {
    {
        .draw = Circle_draw,
        .moveto = Circle_moveto,
        .destroy = Circle_destroy,
    }
};

struct Shape* Circle_new(int x, int y, int radius){
    puts("[C] Creating a new circle");
    struct Circle* object = (struct Circle*)malloc(
        sizeof(struct Circle));
    object->super.funTable = (struct ShapeFunTable*)&circleFunTable;
    object->x = x;
    object->y = y;
    object->radius = radius;
    PRINT_CIRCLE(object);
    puts("[C] Done!");

    return (struct Shape*)object;
}


#define SHAPE_DRAW(object)                  \
    (((struct Shape*)(object))->funTable->draw((struct Shape*)(object)))

#define SHAPE_MOVETO(object, x, y)                  \
    (((struct Shape*)(object))->funTable->moveto(   \
        (struct Shape*)(object), (x), (y)))

#define RECTANGLE_SETWIDTH(object, width)               \
    ((struct RectangleFunTable*)((                      \
        struct Shape*)(object))->funTable)->set_width(  \
            (struct Shape*)(object), (width))

#define SHAPE_DESTROY(object)                       \
    (((struct Shape*)(object))->funTable->destroy(  \
        (struct Shape*)(object)))

/* A function taht uses a Shape polymophically */
void handle_shape(struct Shape* object){
    puts("[C] Handling shape polymorphically");
    SHAPE_MOVETO(object, 0, 0);
    puts("[C] Done!");
}


// ----------------
//   Main Driver
// ----------------
int main(){
    struct Shape* shapes[2];
    /* using shapes polymorphically */
    shapes[0] = Rectangle_new(20, 21, 123, 321);
    shapes[1] = Circle_new(21, 12, 2022);
    for(int i=0; i < 2; i++){
        SHAPE_DRAW(shapes[i]);
        handle_shape(shapes[i]);
    }

    /* accessing Rectangle specific data */
    struct Rectangle* rect = (struct Rectangle*)Rectangle_new(1, 2, 3, 4);
    RECTANGLE_SETWIDTH(rect, 5);
    SHAPE_DRAW(rect);
    SHAPE_DESTROY(rect);

    for(int i=0; i < 2; i++){
        SHAPE_DESTROY(shapes[i]);
    }

    return EXIT_SUCCESS;
}
