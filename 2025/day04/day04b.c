#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct
{
    int size;
    bool **cells;
} Grid;

char *get_input()
{
    FILE *file = fopen("../inputs/input04.txt", "rb");

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

Grid *parse_grid(char *input)
{
    Grid *grid = malloc(sizeof(Grid));
    grid->size = strchr(input, '\n') - input;
    grid->cells = malloc(grid->size * sizeof(bool *));

    for (size_t y = 0; y < grid->size; y++)
    {
        grid->cells[y] = malloc(grid->size * sizeof(bool));
        for (size_t x = 0; x < grid->size; x++)
        {
            grid->cells[y][x] = input[y * (grid->size + 1) + x] == '@';
        }
    }

    return grid;
}

void free_grid(Grid *grid)
{
    for (size_t i = 0; i < grid->size; i++)
    {
        free(grid->cells[i]);
    }

    free(grid->cells);
    free(grid);
}

unsigned int count_neighbors(Grid *grid, int x0, int y0)
{
    static int neighbors[8][2] = {{-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}};

    unsigned int neighbor_count = 0;

    for (size_t i = 0; i < 8; i++)
    {
        int x = x0 + neighbors[i][0];
        int y = y0 + neighbors[i][1];

        if (x >= 0 && y >= 0 && x < grid->size && y < grid->size)
        {
            neighbor_count += grid->cells[y][x];
        }
    }

    return neighbor_count;
}

int main()
{
    char *input = get_input();

    if (!input)
    {
        perror("Failed to read input file");
        return EXIT_FAILURE;
    }

    Grid *grid = parse_grid(input);

    unsigned int total_accessible_roll_count = 0;
    unsigned int accessible_roll_count = 0;

    do
    {
        accessible_roll_count = 0;

        for (size_t y = 0; y < grid->size; y++)
        {
            for (size_t x = 0; x < grid->size; x++)
            {
                if (grid->cells[y][x] && count_neighbors(grid, x, y) < 4)
                {
                    grid->cells[y][x] = 0;
                    accessible_roll_count++;
                }
            }
        }

        total_accessible_roll_count += accessible_roll_count;
    } while (accessible_roll_count > 0);

    printf("Day 3 Part 2: %u\n", total_accessible_roll_count);

    free(input);
    free(grid);

    return EXIT_SUCCESS;
}