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

int rotate(int dial, char direction)
{
    dial = dial + direction;
    return dial < 0
               ? DIAL_SIZE - 1
           : dial >= DIAL_SIZE
               ? 0
               : dial;
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

        for (size_t i = 0; i < distance; i++)
        {
            dial = rotate(dial, direction);

            if (dial == 0)
            {
                password++;
            }
        }
    }

    printf("Day 1 Part 2: %i\n", password);

    return EXIT_SUCCESS;
}