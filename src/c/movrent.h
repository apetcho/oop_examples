#ifndef _MOVIES_RENTAL_H
#define _MOVIES_RENTAL_H
#include<stddef.h>
#include<stdio.h>

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

// Generic vector class
Vector* Vector_create();
void Vector_destroy(Vector*);
void* Vector_get_item(Vector*, size_t);
void Vector_set_item(Vector*, size_t, void*);
size_t Vector_get_size(Vector*);
size_t Vector_get_capacity(Vector*);
void Vector_set_capacity(Vector*, size_t);
char* Vector_to_string(Vector*);
void Vector_print(const Vector*);
size_t Vector_fget(FILE*, Vector*);
size_t Vector_fput(FILE*, const Vector*);
void Vector_clear(Vector*);


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

// Movie class
Movie* Movie_create();
void Movie_destroy(Movie*);
char* Movie_to_string(Movie*);
void Movie_print(const Movie*);
size_t Movie_fget(FILE*, Movie*);
size_t Movie_fput(FILE*, const Movie*);
char* Movie_get_title(const Movie*);
int Movie_get_year(const Movie*);
char* Movie_get_production(const Movie*);
Person* Movie_get_director(const Movie*);
Vector* Movie_get_stars(const Movie*);
void Movie_set_title(Movie*, const char*);
void Movie_set_year(Movie*, int);
void Movie_set_production(Movie*, const char*);
void Movie_set_director(Movie*, const Person*);
void Movie_set_stars(Movie*, const Vector*);

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

// MRObject abstract class

// MovieRental class


#endif
