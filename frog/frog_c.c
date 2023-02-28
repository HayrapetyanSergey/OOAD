#include <stdio.h>

typedef struct Frog Frog;

struct Frog {
    int is_hungry;
    int is_asleep;
    int grass_length;
};

void frog_live(Frog *frog) {
    if (frog->is_asleep) {
        printf("The frog is sleeping.\n");
    } else if (frog->is_hungry) {
        frog_eat(frog);
    } else {
        frog_walk_and_eat(frog);
    }
}

void frog_eat(Frog *frog) {
    if (frog->grass_length > 0) {
        frog->grass_length--;
        frog->is_hungry = 0;
        printf("The frog ate some grass.\n");
    } else {
        printf("There is no grass left for the frog to eat.\n");
    }
}

void frog_walk_and_eat(Frog *frog) {
    if (frog->grass_length > 0) {
        frog->grass_length--;
        printf("The frog walked and ate some grass.\n");
    } else {
        printf("There is no grass left for the frog to eat.\n");
    }
}

void frog_sleep(Frog *frog) {
    frog->is_asleep = 1;
    printf("The frog is sleeping.\n");
}

void frog_wake_up(Frog *frog) {
    frog->is_asleep = 0;
    printf("The frog woke up.\n");
}

void frog_rain(Frog *frog) {
    frog->grass_length += 5;
    printf("It rained and the grass grew longer.\n");
}