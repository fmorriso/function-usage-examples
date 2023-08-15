import inspect
import sys


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def describe_pet(animal_type: str, pet_name: str):
    """Display information about a pet."""
    print(f"\n{inspect.getframeinfo(inspect.currentframe()).function}")
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


def describe_pet_with_defaults(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\n{inspect.getframeinfo(inspect.currentframe()).function}")
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# ----------------------------------------------------------------------------------------


def pets_default_args():
    describe_pet_with_defaults(pet_name="willie")


def pets_first_version():
    print(f"\n{inspect.getframeinfo(inspect.currentframe()).function}")
    describe_pet("hamster", "harry")


def pets_positional_args():
    print(f"\n{inspect.getframeinfo(inspect.currentframe()).function}")
    describe_pet(animal_type="hamster", pet_name="harry")


if __name__ == "__main__":
    print(f"Python version: {get_python_version()}")
    # pets_first_version()
    # pets_positional_args()
    # pets_default_args()
    pets_default_args()
