# 代码生成时间: 2025-09-29 00:01:07
import requests

"""
Project management tool using Python and Requests framework.
This tool allows for basic project management tasks such as creating,
updating, and deleting projects.

Attributes:
    None

Methods:
    create_project(name, description): Creates a new project.
    update_project(id, name=None, description=None): Updates an existing project.
    delete_project(id): Deletes a project.
    get_project(id): Retrieves a project by ID.
    list_projects(): Retrieves a list of all projects.
"""

class ProjectManagementTool:
    def __init__(self, base_url):
        """Initializes the ProjectManagementTool with the base URL."""
        self.base_url = base_url

    def create_project(self, name, description):
        """Creates a new project.

        Args:
            name (str): The name of the project.
            description (str): The description of the project.

        Returns:
            dict: The created project data.
        """
        url = f"{self.base_url}/projects"
        data = {"name": name, "description": description}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def update_project(self, id, name=None, description=None):
        """Updates an existing project.

        Args:
            id (int): The ID of the project to update.
            name (str, optional): The new name of the project. Defaults to None.
            description (str, optional): The new description of the project. Defaults to None.

        Returns:
            dict: The updated project data.
        """
        url = f"{self.base_url}/projects/{id}"
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        response = requests.patch(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete_project(self, id):
        """Deletes a project.

        Args:
            id (int): The ID of the project to delete.

        Returns:
            bool: Whether the deletion was successful.
        """
        url = f"{self.base_url}/projects/{id}"
        response = requests.delete(url)
        response.raise_for_status()
        return True

    def get_project(self, id):
        """Retrieves a project by ID.

        Args:
            id (int): The ID of the project to retrieve.

        Returns:
            dict: The project data.
        """
        url = f"{self.base_url}/projects/{id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def list_projects(self):
        """Retrieves a list of all projects.

        Returns:
            list: A list of project data.
        """
        url = f"{self.base_url}/projects"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

# Example usage:
if __name__ == "__main__":
    tool = ProjectManagementTool("https://example.com/api")
    try:
        project = tool.create_project("New Project", "This is a new project.")
        print("Created project:", project)
        # Update project
        updated_project = tool.update_project(project["id"], name="Updated Project")
        print("Updated project:", updated_project)
        # Get project by ID
        project = tool.get_project(updated_project["id"])
        print("Retrieved project:", project)
        # List all projects
        projects = tool.list_projects()
        print("List of projects:", projects)
        # Delete project
        tool.delete_project(updated_project["id"])
    except requests.RequestException as e:
        print("An error occurred: ", e)