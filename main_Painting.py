# main_Painting.py
# Snikhadha Sinha
# 10/01/2026

from objects_Painting import (
    PortraitPainting,
    LandscapePainting,
    AbstractPainting
)


def main():

    paintings = []
    add_another = "y"

    print("Painting Gallery Program")
    print("------------------------")

    while add_another.lower() == "y":

        print("\n1. Portrait Painting")
        print("2. Landscape Painting")
        print("3. Abstract Painting")

        while True:

            choice = input("\nChoose a painting type (1-3): ")

            if choice in ["1", "2", "3"]:
                break

            print("Invalid choice. Please enter 1, 2, or 3.")

        title = input("Title: ")
        medium = input("Medium: ")

        while True:
            try:
                hours = int(input("Hours: "))
                minutes = int(input("Minutes: "))

                if hours >= 0 and minutes >= 0:
                    break

                print("Hours and minutes must be non-negative.")

            except ValueError:
                print("Please enter valid numbers.")
            except ValueError:
                print("Please enter a valid number.")

        complexity = input("Complexity Level: ")

        # Create the appropriate subclass object
        if choice == "1":

            subject_name = input("Subject Name: ")

            painting = PortraitPainting(
                title,
                medium,
                hours,
                minutes,
                complexity,
                subject_name
            )

        elif choice == "2":

            location = input("Location: ")

            painting = LandscapePainting(
                title,
                medium,
                hours,
                minutes,
                complexity,
                location
            )

        else:

            theme = input("Theme: ")

            painting = AbstractPainting(
                title,
                medium,
                hours,
                minutes,
                complexity,
                theme
            )

        paintings.append(painting)

        while True:
            add_another = input(
                "\nWould you like to add another painting? (y/n): "
            ).lower()

            if add_another in ["y", "n"]:
                break

            print("Please enter y or n.")

    # Display all paintings
    print("\n\nPAINTING GALLERY")
    print("=" * 60)

    for painting in paintings:

        print("\n--- Painting Information ---")
        print(painting.describePainting())

    print("\nThank you for using the Painting Gallery Program!")


if __name__ == "__main__":
    main()