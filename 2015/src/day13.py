from day_abstract import DayAbstract
from itertools import permutations


class Day13(DayAbstract):
    def __init__(self, data: str) -> None:
        super().__init__(data)

    def parse(self) -> list[dict]:
        self.people = set()

        def extract(line: str) -> dict:
            items = line[:-1].split(" ")
            src = items[0]
            dst = items[-1]
            factor = 1 if items[2] == "gain" else -1
            happiness = factor * int(items[3])

            self.people.add(src)
            self.people.add(dst)

            return {"src": src, "dst": dst, "happiness": happiness}

        return list(map(extract, self.data.split("\n")))

    def part_one(self) -> int:
        preferences = self.parse()
        happinesses = []

        for permutation in permutations(self.people):
            happinesses_by_person = dict.fromkeys(self.people, 0)

            for preference in preferences:
                index_of_src = permutation.index(preference["src"])
                index_of_dst = permutation.index(preference["dst"])

                if index_of_dst in [
                    (index_of_src + 1) % len(permutation),
                    (index_of_src - 1) % len(permutation),
                ]:
                    happinesses_by_person[preference["src"]] += preference["happiness"]

            happinesses.append(sum(happinesses_by_person.values()))

        return max(happinesses)

    def part_two(self) -> int:
        preferences = self.parse()
        happinesses = []

        for person in self.people:
            preferences.append({"src": "Me", "dst": person, "happiness": 0})
            preferences.append({"src": person, "dst": "Me", "happiness": 0})

        self.people.add("Me")

        for permutation in permutations(self.people):
            happinesses_by_person = dict.fromkeys(self.people, 0)

            for preference in preferences:
                index_of_src = permutation.index(preference["src"])
                index_of_dst = permutation.index(preference["dst"])

                if index_of_dst in [
                    (index_of_src + 1) % len(permutation),
                    (index_of_src - 1) % len(permutation),
                ]:
                    happinesses_by_person[preference["src"]] += preference["happiness"]

            happinesses.append(sum(happinesses_by_person.values()))

        return max(happinesses)
