import argparse
import random
import string
from typing import List


class RandomPasswordGenerator:
    """Generates random passwords with customizable character sets."""

    def __init__(
        self,
        length: int,
        count: int,
        *,
        disable_letters: bool = False,
        disable_uppercase: bool = False,
        disable_numbers: bool = False,
        disable_special: bool = False,
    ):
        """
        Initialize password generator with specified constraints.

        :param length: Length of each password
        :param count: Number of passwords to generate
        :param disable_letters: Exclude letters from character set
        :param disable_uppercase: Exclude uppercase letters (only effective if letters are enabled)
        :param disable_numbers: Exclude numbers from character set
        :param disable_special: Exclude special characters from character set
        """
        self._validate_inputs(length, count)

        self.characters = self._build_character_set(
            disable_letters, disable_uppercase, disable_numbers, disable_special
        )
        self.length = length
        self.count = count

    def __repr__(self) -> str:
        """Official string representation of the generator instance."""
        return (
            f"RandomPasswordGenerator(length={self.length}, count={self.count}, "
            f"character_set_size={len(self.characters)})"
        )

    @staticmethod
    def _validate_inputs(length: int, count: int) -> None:
        """Validate input parameters."""
        if count <= 0:
            raise ValueError("Password count must be at least 1")
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")

    @staticmethod
    def _build_character_set(
        no_letters: bool, no_upper: bool, no_numbers: bool, no_special: bool
    ) -> str:
        """Construct character set based on enabled options."""
        chars = []

        if not no_letters:
            chars.append(string.ascii_lowercase if no_upper else string.ascii_letters)
        if not no_numbers:
            chars.append(string.digits)
        if not no_special:
            chars.append("!@#$%^&*()")

        if not chars:
            raise ValueError("At least one character set must be enabled")

        return "".join(chars)

    def generate_password(self) -> str:
        """Generate a single random password."""
        return "".join(random.choices(self.characters, k=self.length))

    def generate_passwords(self) -> List[str]:
        """Generate multiple passwords based on configured count."""
        return [self.generate_password() for _ in range(self.count)]


def main():
    """Command line interface for password generation."""
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Password configuration arguments
    parser.add_argument(
        "-l", "--length", type=int, default=12, help="Length of each password"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of passwords to generate"
    )

    # Character set exclusion arguments
    char_group = parser.add_argument_group("Character set options")
    char_group.add_argument(
        "--no-letters", action="store_true", help="Exclude letters from character set"
    )
    char_group.add_argument(
        "--no-upper", action="store_true", help="Exclude uppercase letters"
    )
    char_group.add_argument(
        "--no-numbers", action="store_true", help="Exclude numeric characters"
    )
    char_group.add_argument(
        "--no-special", action="store_true", help="Exclude special characters"
    )

    args = parser.parse_args()

    try:
        generator = RandomPasswordGenerator(
            length=args.length,
            count=args.count,
            disable_letters=args.no_letters,
            disable_uppercase=args.no_upper,
            disable_numbers=args.no_numbers,
            disable_special=args.no_special,
        )

        print(f"\nGenerated {args.count} password(s):")
        for password in generator.generate_passwords():
            print(f"  {password}")

    except ValueError as e:
        print(f"\nError: {e}")
        parser.print_help()


if __name__ == "__main__":
    main()
