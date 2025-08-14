#Sikai Sellers Cis261 Movie Guide Part 2
def create_file():
    """Create and populate the movies.txt file with initial titles."""
    with open("movies.txt", "w") as file:
        file.write("Cat on a Hot Tin Roof\n")
        file.write("On the Waterfront\n")
        file.write("Monty Python and the Holy Grail\n")

def load_movies():
    """Load movies from the file into a list."""
    try:
        with open("movies.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_movies(movies):
    """Save the current list of movies back to the file."""
    with open("movies.txt", "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_menu():
    """Display the heading and command menu."""
    print("The Movie List program\n")
    print("Command MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit the program\n")

def list_movies(movies):
    """Display all movies in the list."""
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}. {movie}")
    print()

def add_movie(movies):
    """Add a new movie to the list."""
    title = input("Movie: ").strip()
    if title:
        movies.append(title)
        print(f"{title} was added.\n")
    else:
        print("No title entered. Nothing added.\n")

def delete_movie(movies):
    """Delete a movie by its number."""
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies):
            removed = movies.pop(number - 1)
            print(f"{removed} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main():
    create_file()
    movies = load_movies()
    display_menu()

    while True:
        command = input("Command: ").strip().lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
            save_movies(movies)
        elif command == "del":
            delete_movie(movies)
            save_movies(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()


            


