def greet_user():
  """Takes user's first and last name, concatenates them, and prints a greeting."""
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  full_name = first_name + " " + last_name
  print()
  print(f"Hello, {full_name}! Welcome to the Python program.")

if __name__ == "__main__":
  greet_user()