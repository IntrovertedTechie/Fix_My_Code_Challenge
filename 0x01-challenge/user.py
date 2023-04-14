#!/usr/bin/python3
""" 
User class
"""

class User():
    """ 
    This class represents a user with an email address.
    """

    def __init__(self):
        """ 
        Initializes a new User object with an email address set to None.
        """
        self.__email = None

    @property
    def email(self):
        """ 
        Gets the email address of the user.

        Returns:
        The email address of the user as a string.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """ 
        Sets the email address of the user.

        Args:
        value (str): The email address to set.

        Raises:
        TypeError: If the value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


