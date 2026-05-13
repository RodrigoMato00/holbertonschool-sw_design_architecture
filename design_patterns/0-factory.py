#!/usr/bin/env python3


class Bus:
    def mode(self) -> str:
        return "road"


class Train:
    def mode(self) -> str:
        return "rails"


class Bike:
    def mode(self) -> str:
        return "lane"


class Scooter:
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self) -> None:
        self._registry: dict[str, type] = {}
        self.register_kind("bus", Bus)
        self.register_kind("train", Train)
        self.register_kind("bike", Bike)

    def register_kind(self, name: str, cls: type) -> None:
        self._registry[name] = cls

    def create(self, kind: str):
        cls = self._registry[kind]
        return cls()


def main() -> None:
    factory = VehicleFactory()
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()


def main() -> None:
    factory = VehicleFactory()
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
