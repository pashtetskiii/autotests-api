from enum import Enum

class AllureFeature(str, Enum):
    COURSES = "Courses"
    USERS = "Users"
    FILES = "Files"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"