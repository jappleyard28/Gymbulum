from flet import  *
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from views.CreateWorkout import CreateWorkoutView

def main(page: Page):
    page.title = "Gymbulum"
    '''page.horizontal_alignment = 'center'
    page.vertical_alignment = ' center'
    page.window_width=500
    page.window_height=700
    container = Container(
        width=500,
        height=500,
        bgcolor='red',
        border_radius=35,
    )
    page.add(container)'''

    def route_change(e: RouteChangeEvent):
        page.views.clear()
        
        # Home
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    Text(value='Home', size=30),
                    ElevatedButton(text='Create Workout', on_click=lambda _: page.go('/create_workout')),
                    ElevatedButton(text='Calendar', on_click=lambda _: page.go('/calendar')),
                    ElevatedButton(text='Settings', on_click=lambda _: page.go('/settings')),
                    ElevatedButton(text='Progress Tracking', on_click=lambda _: page.go('/progress')),
                    ElevatedButton(text='Friends', on_click=lambda _: page.go('/friends')),
                    ElevatedButton(text='Create Target', on_click=lambda _: page.go('/create_target')),
                    ElevatedButton(text='Current Targets', on_click=lambda _: page.go('/current_targets')),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        # Create Workout Page
        if page.route == '/create_workout':
            page.views.append(
                View(
                    route='/create_workout',
                    controls=[
                        AppBar(title=Text('Create Workout'), bgcolor='blue'),
                        Text(value='Create Workout', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        # Calendar page
        if page.route == '/calendar':
            page.views.append(
                View(
                    route='/calendar',
                    controls=[
                        AppBar(title=Text('Calendar'), bgcolor='blue'),
                        Text(value='Calendar', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        # Settings page
        if page.route == '/settings':
            page.views.append(
                View(
                    route='/settings',
                    controls=[
                        AppBar(title=Text('Settings'), bgcolor='blue'),
                        Text(value='Settings', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        # Progress tracking page
        if page.route == '/progress':
            page.views.append(
                View(
                    route='/progress',
                    controls=[
                        AppBar(title=Text('Progress Tracking'), bgcolor='blue'),
                        Text(value='Progress Tracking', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        # Friends page
        if page.route == '/friends':
            page.views.append(
                View(
                    route='/friends',
                    controls=[
                        AppBar(title=Text('Friends'), bgcolor='blue'),
                        Text(value='Friends', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        # Create target page
        if page.route == '/create_target':
            page.views.append(
                View(
                    route='/create_target',
                    controls=[
                        AppBar(title=Text('Create target'), bgcolor='blue'),
                        Text(value='Create target', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        # Current targets page
        if page.route == '/current_targets':
            page.views.append(
                View(
                    route='/current_targets',
                    controls=[
                        AppBar(title=Text('Current targets'), bgcolor='blue'),
                        Text(value='Current targets', size=30),
                        ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        
        page.update()

    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
    

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    app(target=main)