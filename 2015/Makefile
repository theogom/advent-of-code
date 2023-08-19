SRC_DIR = src

.PHONY: tests

all: day

day:
ifndef DAY
	@python3 $(SRC_DIR)/__main__.py
else
	@python3 $(SRC_DIR)/__main__.py --day $(DAY)
endif

day%:
	@python3 $(SRC_DIR)/__main__.py --day $*

tests:
	@python3 -m unittest