#ifndef EXAMPLE_H
#define EXAMPLE_H

#define MAX_SIZE 100
#define VERSION "1.0"

typedef struct {
    int id;
    char name[50];
} Person;

void init_person(Person *p, int id, const char *name);
void print_person(const Person *p);

#endif
789