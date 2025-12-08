CC = gcc
CFLAGS = -Wall -Wextra

DAY_SOURCES = $(wildcard day*/day*.c)
DAY_TARGETS = $(DAY_SOURCES:.c=)

.PHONY: all clean

all: build

build: $(DAY_TARGETS)

run: build
	@for target in $(DAY_TARGETS); do \
		./$$target; \
	done

run-day%: build
	@./day$*/day$*a
	@./day$*/day$*b

day%/day%a: day%/day%a.c
	$(CC) $(CFLAGS) -o $@ $<

day%/day%b: day%/day%b.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(DAY_TARGETS)