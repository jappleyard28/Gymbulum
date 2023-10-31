from flet import *

def CreateWorkoutView():
    AppBar(title=Text('Create Workout'), bgcolor='blue'),
    Text(value='Create Workout', size=30),
    ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))