#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *get_input()
{
    FILE *file = fopen("../inputs/input03.txt", "rb");

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

size_t max(char *values, size_t start_index, size_t end_index)
{
    char max_index = start_index;

    for (size_t i = start_index; i < end_index; i++)
    {
        if (values[i] > values[max_index])
        {
            max_index = i;
        }
    }

    return max_index;
}

unsigned long get_max_joltage(char *bank, size_t bank_size, size_t battery_count)
{
    unsigned long joltage = 0;
    size_t battery_index = -1;

    for (size_t i = 0; i < battery_count; i++)
    {
        battery_index = max(bank, battery_index + 1, bank_size - battery_count + i + 1);
        joltage = joltage * 10 + (bank[battery_index] - '0');
    }

    return joltage;
}

int main()
{
    char *input = get_input();

    if (!input)
    {
        perror("Failed to read input file");
        return EXIT_FAILURE;
    }

    unsigned long total_joltage = 0;
    char *bank = strtok(input, "\n");
    size_t bank_size = strlen(bank);

    for (; bank != NULL; bank = strtok(NULL, "\n"))
    {
        total_joltage += get_max_joltage(bank, bank_size, 12);
    }

    free(input);

    printf("Day 3 Part 2: %lu\n", total_joltage);

    return EXIT_SUCCESS;
}