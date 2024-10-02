"""
Exercise 4
"""

from pathlib import Path

def create_exercise_liste(project_assignment_start:int, totall_exercises: int)-> None:
    
    exercises = [f"Exercise{i}" if i < project_assignment_start else f"Exercise {i}a" if i==j else f"Exercise {i}b"
                 for i in range(1, totall_exercises + 1)
                 for j in range(project_assignment_start, totall_exercises +1) if i < project_assignment_start or i==j
    ]
    return exercises


def create_folder(students:str, exercises:str):
    current_dir = Path.cwd()/ 'Projects'
    
    for student in students:

        for exercise in exercises:

            folder_path = current_dir/ f"Exercise {exercise}"/ student
            folder_path.mkdir(parents= True, exist_ok=True)
            print(f"{folder_path} created succesfully")
            
totall_exercises=4
project_assignment_start=3

students = ["Ole", "Sarah"]

exercises = ["1","2","3a","3b","4a","4b"]

create_folder(students, exercises)










