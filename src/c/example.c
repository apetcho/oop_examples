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

    printf("(C) [Rectangle] Width = %d, Height = %d, at position (%d, %d)!\n",
        rect->width, rect->height, rect->x, rect->y);
}
