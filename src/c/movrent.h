#ifndef _MOVIES_RENTAL_H
#define _MOVIES_RENTAL_H
#include<stddef.h>
#include<stdio.h>
#include<assert.h>

/** Forward declaration of VTables */
typedef struct VectorVTbale VectorVTbale;
typedef struct PersonVTable PersonVTable;
typedef struct MovieVTable MovieVTable;
typedef struct CustomerVTable CustomerVTable;
typedef struct MovieRentalVTable MovieRentalVTable;

/** Forward declaration of classes */
typedef struct Vector Vector;
typedef struct Person Person;
typedef struct Movie Movie;
typedef struct Customer Customer;
typedef struct MovieRental MovieRental;

/* Type enumartion and union */
typedef enum {
    UNKNOWN = 0,
    PERSON,
    CUSTOMER,
    MOVIE,
    MOVIE_RENTAL,
} ObjectEnum;

typedef struct Object Object;

// Generic vector class
Vector* Vector_create();
void Vector_destroy(Vector*);
Object* Vector_get_item(Vector*, size_t);
void Vector_set_item(Vector*, size_t, Object*);
size_t Vector_get_size(Vector*);
size_t Vector_get_capacity(Vector*);
void Vector_set_capacity(Vector*, size_t);
char* Vector_to_string(Vector*);
void Vector_print(const Vector*);
size_t Vector_fget(FILE*, Vector*);
size_t Vector_fput(FILE*, const Vector*);
void Vector_clear(Vector*);

struct VectorVTable{
    Vector* (*create)(void);
    void (*destroy)(Vector*);
    void (*get)(Vector*, size_t);
    void (*set)(Vector*, size_t, Object*);
    size_t (*size)(Vector*);
    size_t (*capacity)(Vector*);
    char* (*to_string)(Vector*);
    void (*print)(Vector*);
    size_t (*fget)(FILE*, Vector*);
    size_t (*fput)(FILE*, const Vector*);
    void (*clear)(Vector*);
};


// Person class
Person* Person_create();
void Person_destroy(Person*);
char* Person_to_string(Person*);
void Person_print(const Person*);
size_t Person_fget(FILE*, Person*);
size_t Person_fput(FILE*, const Person*);
char* Person_get_first_name(const Person*);
char* Person_get_last_name(const Person*);
char* Person_get_email(const Person*);
void Person_set_first_name(Person*, const char*);
void Person_set_last_name(Person*, const char*);
void Person_set_email(Person*, const char*);

struct PersonVTable{
    Person* (*create)(void);
    void (*destroy)(Person*);
    char* (*to_string)(Person*);
    void (*print)(Person*);
    size_t (*fget)(FILE*, Person*);
    size_t (*fput)(FILE*, const Person*);
    char* (*set_first_name)(const Person*);
    char* (*set_last_name)(const Person*);
    char* (*set_email)(const Person*);
    void (*get_first_name)(Person*);
    void (*get_last_name)(Person*);
    void (*get_email)(Person*);
};

// Movie class
Movie* Movie_create();
void Movie_destroy(Movie*);
char* Movie_to_string(Movie*);
void Movie_print(const Movie*);
size_t Movie_fget(FILE*, Movie*);
size_t Movie_fput(FILE*, const Movie*);
char* Movie_get_title(const Movie*);
int Movie_get_year(const Movie*);
char* Movie_get_company(const Movie*);
Person* Movie_get_director(const Movie*);
Vector* Movie_get_stars(const Movie*);
void Movie_set_title(Movie*, const char*);
void Movie_set_year(Movie*, int);
void Movie_set_company(Movie*, const char*);
void Movie_set_director(Movie*, const Person*);
void Movie_set_stars(Movie*, const Vector*);

struct MovieVTable{
    Movie* (*create)(void);
    void (*destroy)(Movie*);
    char* (*to_string)(Movie*);
    void (*print)(Movie*);
    size_t (*fget)(FILE*, Movie*);
    size_t (*fput)(FILE*, const Movie*);
    char* (*get_title)(const Movie*);
    int (*get_year)(const Movie*);
    char* (*get_company)(const Movie*);
    Person* (*get_director)(const Movie*);
    Vector* (*get_stars)(const Movie*);
    void (*set_title)(Movie*);
    void (*set_year)(Movie*);
    void (*set_company)(Movie*);
    void (*set_director)(Movie*);
    void (*set_stars)(Movie*);
};


// Customer class
Customer* Customer_create();
void Customer_destroy(Customer*);
char* Customer_to_string(Customer*);
void Customer_print(const Customer*);
size_t Customer_fget(FILE*, Customer*);
size_t Customer_fput(FILE*, const Customer*);
Person* Customer_get_info(const Customer*);
Vector* Customer_get_movies(const Customer*);
void Customer_set_info(Customer*, Person*);
void Customer_set_movies(Customer*, Vector*);

struct CustomerVTable{
    Customer* (*create)(void);
    void (*destroy)(Customer*);
    char* (*to_string)(Customer*);
    void (*print)(Customer*);
    size_t (*fget)(FILE*, Customer*);
    size_t (*fput)(FILE*, const Customer*);
    Person* (*get_info)(const Customer*);
    Vector* (*get_movies)(const Customer*);
    void (*set_info)(Customer*);
    void (*set_movies)(Customer*);
};

// AbstractObject abstract class
typedef struct {
    PersonVTable _pvtable;
    MovieVTable _mvtable;
    CustomerVTable _cvtable;
} AbstractObject;
/** Don't allow instatiation of Abstract object */
AbstractObject* AbstractObject_create(){ assert(0);}
void AbstractObject_destroy(){}

// MovieRental class
struct MovieRental{
    AbstractObject *super;
    /**/
    Vector* movies;
    Vector* customers;
    char* manager;
};

MovieRental* new_movie_rental();
void del_movie_rental();
Vector* load_customers(const char* filename);
void save_customers(const char* filename);
Vector* load_movies(const char* filename);
void save_movies(const char* filename);

#endif
