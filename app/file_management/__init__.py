# from pathlib import Path

# class DirectoryManager:
#     """
#     Singleton class responsible for managing directory creation and validation.
    
#     Attributes:
#         directory (Path): Path object representing the directory.
#     """
    
#     _instances = {}

#     def __new__(cls, directory):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(DirectoryManager, cls).__new__(cls)
#         return cls._instances[cls]

#     def __init__(self, directory):
#         """
#         Initializes DirectoryManager and ensures the directory exists.

#         Args:
#             directory (str or Path): The directory to manage.
#         """
#         self.directory = Path(directory)
#         self.ensure_directory_exists()

#     def ensure_directory_exists(self):
#         """
#         Ensures the specified directory exists, creating it if necessary.
        
#         Raises:
#             Exception: If the directory cannot be created.
#         """
#         if not self.directory.exists():
#             try:
#                 self.directory.mkdir(parents=True)
#             except Exception as e:
#                 raise Exception(f"Error creating directory {self.directory}: {e}")

#     def get_directory(self):
#         """
#         Returns the directory managed by this instance.

#         Returns:
#             Path: The path of the managed directory.
#         """
#         return self.directory
