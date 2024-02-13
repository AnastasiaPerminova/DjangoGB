from django.shortcuts import render
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


# Create your views here.

def main(request):
    logger.info('Main page accessed')
    html = f'''<!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8"/>
      <title>Main</title>
    </head>
    <body>
      <h1>Django. GeekBrains. Seminars. </h1>
      <h2>Homework_project.</h2>
    </body>
    </html>'''

    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    text = f'''<!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8"/>
      <title>About</title>
    </head>
    <body>
      <h1>It's a page about my django homework_project. </h1>
      
      <p> I've just started to learn Django and homework_1 has been done.</p>
    </body>
    </html>'''
    return HttpResponse(text)
