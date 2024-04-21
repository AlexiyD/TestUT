from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def render_menu(self):
        menu_html = f'<li><a href="{self.url}">{self.name}</a></li>'
        if self.children.exists():
            menu_html += '<ul>'
            for child in self.children.all():
                menu_html += child.render_menu()
            menu_html += '</ul>'
        return menu_html