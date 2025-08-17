from flet import Page, SnackBar, Text, colors

def show_snackbar(page: Page, message: str, color=colors.RED_400):

    page.add(SnackBar(
        content=Text(message, color=colors.WHITE),
        bgcolor=color,
        open=True, 
        duration=3000
    ))
    page.update()