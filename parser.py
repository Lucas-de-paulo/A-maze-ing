"""Parse and validate the A-Maze-ing configuration file."""

class Config:
    """Store and validate the maze configuration."""
    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        output_file: str,
        perfect: bool,
        seed: int | None = None,
    ) -> None:
        """Initialize the configuration with the provided values."""
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed
        self.validate()

    def validate(self) -> None:
        """Validate maze dimensions and entry and exit coordinates."""
        for x, y in (self.entry, self.exit):
            if not (0 <= x < self.width and 0 <= y < self.height):
                raise ValueError(
                    f"Coordinates out of maze bounds {x, y}"
                )

        if self.entry == self.exit:
            raise ValueError(
                f"Coordinates entry and exit they are the same"
            )

        if self.width < 9 or self.height < 7:
            raise ValueError(
                f"The maze is small, the minimum is width: 9 and height: 7"
            )


ALLOWED_KEYS = {
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "OUTPUT_FILE",
    "PERFECT",
    "SEED"
}


def parse_coordinates(value: str) -> tuple[int, int]:
    """Convert a coordinate string into an integer tuple."""
    parts = value.split(",")

    if len(parts) != 2:
        raise ValueError(
            f"Invalid coordinates: {value}"
        )

    return int(parts[0].strip()), int(parts[1].strip())


def parse_bool(value: str) -> bool:
    """Convert a string into a boolean value."""
    if value == "True":
        return True

    if value == "False":
        return False

    raise ValueError(f"Invalid boolean: {value}")


def load_config(path: str) -> Config:
    """Load and parse the maze configuration file."""
    values: dict[str, str] = {}

    try:
        with open(path, "r") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    raise ValueError(f"Line {line_number}: expected KEY=VALUE")

                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()

                if key not in ALLOWED_KEYS:
                    raise ValueError(
                        f"Line {line_number}: unknown key '{key}'"
                    )

                values[key] = value
    except OSError as error:
        raise ValueError(
            f"Cannot read config file: {error}"
        )

    try:
        config = Config(
            width=int(values["WIDTH"]),
            height=int(values["HEIGHT"]),
            entry=parse_coordinates(values["ENTRY"]),
            exit=parse_coordinates(values["EXIT"]),
            output_file=values["OUTPUT_FILE"],
            perfect=parse_bool(values["PERFECT"]),
            seed=(
                int(values["SEED"])
                if "SEED" in values
                else None
            ),
        )
    except ValueError as e:
        raise ValueError(
            f"Invalid configuration value: {e}"
        )
    except KeyError as e:
        raise ValueError(
            f"Missing information '{e.args[0]}' in {path}"
        )

    return config


if __name__ == '__main__':
    config = load_config("config.txt")

    print(config.width)
    print(config.height)
    print(config.entry)
    print(config.exit)
    print(config.output_file)
    print(config.perfect)
    print(config.seed)
