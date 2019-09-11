from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):

	return HttpResponse("<h1>Hiç olmazsa yılda bi gün<br>An beni, al bi karanfil tak<br>Benden olsun, bi sigara yak<br>Bana kor olsun sigara yak<br><br>Sıla'ya selam Django'ya devam</h1>")