"""Pseudocode
Begin program

Document the module using a module level docstring.

Define a User class to represent a user account.

Define a constructor method that stores the user's id, username, and email.

Define methods to return the user's id, username, and email.

Create a User object with example values.

Call the method to retrieve the user’s ID.

Display the user ID.

End program"""




"""
Module: User Management
Description: This module provides functionality for managing user accounts.

Author: John Doe <johndoe@example.com>
Version: 1.0.0
"""
class User:
    """
    Class representing a user account.

    Attributes:
        - id (int): The unique identifier of the user.
        - username (str): The username associated with the account.
        - email (str): The email address of the user.
    """

    def __init__(self, id: int, username: str, email: str):
        """
        Initialize a User object.

        Args:
            - id (int): The unique identifier of the user.
            - username (str): The username associated with the account.
            - email (str): The email address of the user.
        """
        self.id = id
        self.username = username
        self.email = email

    def get_id(self) -> int:
        """
        Get the user's unique identifier.

        Returns:
            - int: The unique identifier of the user.
        """
        return self.id

    def get_username(self) -> str:
        """
        Get the username associated with the account.

        Returns:
            - str: The username of the user.
        """
        return self.username

    def get_email(self) -> str:
        """
        Get the email address of the user.

        Returns:
            - str: The email address of the user.
        """
        return self.email

# Usage Example
user = User(1, "johndoe", "johndoe@example.com")
user_id = user.get_id()
print(f"User ID: {user_id}")