#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DIAL_SIZE 100

char *get_input()
{
    FILE *file = fopen("inputs/input01.txt", "rb");

    if (!file)
    {
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    size_t size = ftell(file);
    rewind(file);

    char *buffer = malloc(size + 1);
    fread(buffer, 1, size, file);
    buffer[size] = '\0';

    fclose(file);

    return buffer;
}

int positive_modulo(int a, int b)
{
    return ((a % b) + b) % b;
}

int main()
{
    char *input = get_input();

    if (!input)
    {
        perror("Failed to read input file");
        return EXIT_FAILURE;
    }

    int password = 0;
    int dial = 50;

    for (char *instruction = strtok(input, "\n"); instruction != NULL; instruction = strtok(NULL, "\n"))
    {
        char direction = instruction[0] == 'L' ? -1 : 1;
        unsigned int distance = atoi(instruction + 1);
        int rotation = direction * distance;

        dial = positive_modulo(dial + rotation, DIAL_SIZE);

        if (dial == 0)
        {
            password++;
        }
    }

    printf("Day 1 Part 1: %i\n", password);

    return EXIT_SUCCESS;
}