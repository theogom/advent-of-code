#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *get_input()
{
    FILE *file = fopen("inputs/input02.txt", "rb");

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

bool is_id_valid(const char *id)
{
    size_t length = strlen(id);

    if (length % 2 != 0)
    {
        return true;
    }

    size_t half_length = length / 2;

    return strncmp(id, id + half_length, half_length) != 0;
}

int main()
{
    char *input = get_input();

    if (!input)
    {
        perror("Failed to read input file");
        return EXIT_FAILURE;
    }

    unsigned long invalid_id_sum = 0;

    for (char *range = strtok(input, ","); range != NULL; range = strtok(NULL, ","))
    {
        unsigned long range_start = 0;
        unsigned long range_end = 0;

        sscanf(range, "%lu-%lu", &range_start, &range_end);

        for (size_t id = range_start; id <= range_end; id++)
        {
            char id_string[32];
            snprintf(id_string, sizeof(id_string), "%lu", id);

            if (!is_id_valid(id_string))
            {
                invalid_id_sum += id;
            }
        }
    }

    printf("Day 2 Part 1: %lu\n", invalid_id_sum);

    free(input);

    return EXIT_SUCCESS;
}