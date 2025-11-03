"""
CP1404 Practical - 7
Estimated time : 2 hours
Actual time: 1.5 hours
Project Management
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = ("- (L)oad projects \n"
        "- (S)ave projects \n"
        "- (D)isplay projects \n"
        "- (F)ilter projects by date) \n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")

def main():
    """Program for a project management that track project completion and project details that user wish to complete."""
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Load {len(projects)} projects from {FILENAME}")
    print(MENU)

    choice =input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
           filename = input("Filename: ")
           projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects,date)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
    if save_choice in ["yes", "y"]:
        save_projects(FILENAME, projects)
        print(f"Projects saved to {FILENAME}.")
    else:
        print("No changes were saved.")
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from the txt file and return a list of project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline() #Skip header line
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects(filename, projects):
    """Save the list of projects to the file in tab-separated format."""
    with open(filename, "w", newline="") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")

def display_projects(projects):
    """Display all projects."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    print("Incomplete projects: ")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Complete Projects: ")
    for project in sorted(complete):
        print(f"  {project}")

def filter_projects_by_date(projects,date):
    """Filter and display projects starting after the given date."""
    try:
        filter_date = datetime.strptime(date, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date >= filter_date]
        print("Filtered projects:")
        for project in sorted(filtered_projects, key=lambda project: project.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyy.")


def add_project(projects):
    """Add a new project to the project list."""
    print("Let's add a new project")
    name = input("Name: ")
    try:
        start_date = datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: "))
        completion_percentage = int(input("Completion Percentage: "))

        projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        print(f"Project '{name}' added successfully!")
    except ValueError:
        print("Invalid input. Ensure priority, cost, and completion percentage are numeric.")


def update_project(projects):
    """Update an existing project."""
    print("\nChoose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i}: {project}")

    try:
        project_index = int(input("Project choice: "))
        if project_index < 0 or project_index >= len(projects):
            print("Invalid selection.")
            return

        project = projects[project_index]
        print(f"\nUpdating project: {project}")

        new_completion_percentage = input("New Percentage (leave blank to keep current): ").strip()
        new_priority = input("New Priority (leave blank to keep current): ").strip()

        if new_completion_percentage:
            project.completion_percentage = int(new_completion_percentage)
        if new_priority:
            project.priority = int(new_priority)

        print(f"Project '{project.name}' updated successfully!")
    except ValueError:
        print("Invalid input. Ensure numbers are entered correctly.")

main()