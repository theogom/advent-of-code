#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 256

int positive_modulo(int a, int b) {
    return ((a % b) + b) % b;
}

int main() {
        char buffer[BUFFER_SIZE];
    int password = 0;
    int dial = 50;
    int dial_size = 100;

    while (fgets(buffer, sizeof(buffer), stdin)) {
        char direction = buffer[0] == 'L' ? -1 : 1;
        int tick = atoi(buffer + 1);
        int rotation = direction * tick;
        
        dial = positive_modulo(dial + rotation, dial_size);

        if (dial == 0) {
            password++;
        }
    }

    printf("Day 1 Part 1: %i\n", password);

    return EXIT_SUCCESS;
}