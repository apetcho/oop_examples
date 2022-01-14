#include<stdlib.h>
#include<stdio.h>
#include<assert.h>

/* Shape abstract interface */
struct Shape {
    struct ShapeFunctTable *funTable;
};
