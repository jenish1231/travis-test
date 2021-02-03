from django.http.response import HttpResponse
from django.views.generic import View, TemplateView


class IndeView(TemplateView):
    template_name = 'users/index.html'
    

async def websocket_view(socket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        await socket.send_text(message)


