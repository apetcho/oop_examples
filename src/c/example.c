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

// never create an instance shape directly: this make it an abstract interface
struct Shape* Shape_new(){ assert(0); }

