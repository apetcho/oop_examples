#ifndef _MOVIES_RENTAL_H
#define _MOVIES_RENTAL_H
#include<stddef.h>
#include<stdio.h>
#include<assert.h>


typedef struct {
    FILE *fp;
}File;

/** Forward declaration of VTables */
typedef struct VectorVTable VectorVTable;
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
Object* Vector_get_item(const Vector*, size_t);
void Vector_set_item(Vector*, size_t, Object*);
size_t Vector_get_size(const Vector*);
size_t Vector_get_capacity(const Vector*);
void Vector_set_capacity(Vector*, size_t);
char* Vector_to_string(const Vector*);
void Vector_print(const Vector*);
size_t Vector_fget(File*, Vector*);
size_t Vector_fput(File*, const Vector*);
void Vector_clear(Vector*);
void Vector_push_back(Vector*, Object*);
Object* Vector_pop_back(Vector*);
void Vector_foreach(Vector*, ForeachCallback Fn);

typedef void (*ForeachCallback)(Object*);

struct VectorVTable{
    Vector* (*create)(void);
    void (*destroy)(Vector*);
    Object* (*get)(const Vector*, size_t);
    void (*set)(Vector*, size_t, Object*);
    size_t (*size)(const Vector*);
    void (*set_capacity)(Vector*, size_t);
    size_t (*get_capacity)(const Vector*);
    char* (*to_string)(const Vector*);
    void (*print)(const Vector*);
    size_t (*fget)(File*, Vector*);
    size_t (*fput)(File*, const Vector*);
    void (*clear)(Vector*);
    void (*push_back)(Vector*, Object*);
    Object* (*pop_back)(Vector*);
    void (*foreach)(Vector*, ForeachCallback);
};

const VectorVTable _vvtable = {
    .create = Vector_create,
    .destroy = Vector_destroy,
    .to_string = Vector_to_string,
    .print = Vector_print,
    .fput = Vector_fput,
    .fget = Vector_fget,
    .get = Vector_get_item,
    .set = Vector_set_item,
    .size = Vector_get_size,
    .set_capacity = Vector_set_capacity,
    .get_capacity = Vector_get_capacity,
    .push_back = Vector_push_back,
    .pop_back = Vector_pop_back,
    .foreach = Vector_foreach,
};

struct Vector{
    VectorVTable *super;
    /**/
    Object *data;
    size_t size;
    size_t capacity;
};

// Person class
Person* Person_create();
void Person_destroy(Person*);
char* Person_to_string(const Person*);
void Person_print(const Person*);
size_t Person_fget(File*, Person*);
size_t Person_fput(File*, const Person*);
char* Person_get_first_name(const Person*);
char* Person_get_last_name(const Person*);
char* Person_get_email(const Person*);
void Person_set_first_name(Person*, const char*);
void Person_set_last_name(Person*, const char*);
void Person_set_email(Person*, const char*);

struct PersonVTable{
    Person* (*create)(void);
    void (*destroy)(Person*);
    char* (*to_string)(const Person*);
    void (*print)(const Person*);
    size_t (*fget)(File*, Person*);
    size_t (*fput)(File*, const Person*);
    void (*set_first_name)(Person*, const char*);
    void (*set_last_name)(Person*, const char*);
    void (*set_email)(Person*, const char*);
    char* (*get_first_name)(const Person*);
    char* (*get_last_name)(const Person*);
    char* (*get_email)(const Person*);
};

const PersonVTable _pvtable = {
    .create = Person_create,
    .destroy = Person_destroy,
    .to_string = Person_to_string,
    .print = Person_print,
    .fget = Person_fget,
    .fput = Person_fput,
    .get_first_name = Person_get_first_name,
    .get_last_name = Person_get_last_name,
    .get_email = Person_get_email,
    .set_first_name = Person_set_first_name,
    .set_last_name = Person_set_last_name,
    .set_email = Person_set_email,
};

struct Person {
    PersonVTable *super;
    /**/
    char* fname;
    char* lname;
    char* email;
};


// Movie class
Movie* Movie_create();
void Movie_destroy(Movie*);
char* Movie_to_string(const Movie*);
void Movie_print(const Movie*);
size_t Movie_fget(File*, Movie*);
size_t Movie_fput(File*, const Movie*);
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
    char* (*to_string)(const Movie*);
    void (*print)(const Movie*);
    size_t (*fget)(File*, Movie*);
    size_t (*fput)(File*, const Movie*);
    char* (*get_title)(const Movie*);
    int (*get_year)(const Movie*);
    char* (*get_company)(const Movie*);
    Person* (*get_director)(const Movie*);
    Vector* (*get_stars)(const Movie*);
    void (*set_title)(Movie*, const char*);
    void (*set_year)(Movie*, int);
    void (*set_company)(Movie*, const char*);
    void (*set_director)(Movie*, const Person*);
    void (*set_stars)(Movie*, const Vector*);
};

const MovieVTable _mvtable = {
    .create = Movie_create,
    .destroy = Movie_destroy,
    .to_string = Movie_to_string,
    .print = Movie_print,
    .fget = Movie_fget,
    .fput = Movie_fput,
    .get_title = Movie_get_title,
    .get_year = Movie_get_year,
    .get_director = Movie_get_director,
    .get_company = Movie_get_company,
    .get_stars = Movie_get_stars,
    .set_title = Movie_set_title,
    .set_year = Movie_set_year,
    .set_director = Movie_set_director,
    .set_company = Movie_set_company,
    .set_stars = Movie_set_stars,
};

struct Movie{
    MovieVTable *super;
    /**/
    char *title;
    Person *director;
    int year;
    char *company;
    Vector* stars;
};



// Customer class
Customer* Customer_create();
void Customer_destroy(Customer*);
char* Customer_to_string(const Customer*);
void Customer_print(const Customer*);
size_t Customer_fget(File*, Customer*);
size_t Customer_fput(File*, const Customer*);
Person* Customer_get_info(const Customer*);
Vector* Customer_get_movies(const Customer*);
void Customer_set_info(Customer*, Person*);
void Customer_set_movies(Customer*, Vector*);

struct CustomerVTable{
    Customer* (*create)(void);
    void (*destroy)(Customer*);
    char* (*to_string)(const Customer*);
    void (*print)(const Customer*);
    size_t (*fget)(File*, Customer*);
    size_t (*fput)(File*, const Customer*);
    Person* (*get_info)(const Customer*);
    Vector* (*get_movies)(const Customer*);
    void (*set_info)(Customer*, Person*);
    void (*set_movies)(Customer*, Vector*);
};

const CustomerVTable _cvtable = {
    .create = Customer_create,
    .destroy = Customer_destroy,
    .to_string = Customer_to_string,
    .print = Customer_print,
    .fget = Customer_fget,
    .fput = Customer_fput,
    .get_info = Customer_get_info,
    .get_movies = Customer_get_movies,
    .set_info = Customer_set_info,
    .set_movies = Customer_set_movies,
};

struct Customer{
    CustomerVTable *super;
    Person* info;
    Vector* movies;
};

// AbstractObject abstract class
typedef struct {
    PersonVTable *pvtable;
    MovieVTable *mvtable;
    CustomerVTable *cvtable;
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
