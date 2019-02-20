from .form import MyForm
from PIL import Image, ImageDraw
from django.shortcuts import render


def IndexView(request):
    if request.method == 'POST':
        form = MyForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            request.session['num'] = black_and_white(request.FILES['image'])
            return render(request,
                          'C:\\Users\\a.rusnak\\PycharmProjects\\AppColors\\AppPil\\color\\templates\\result.html',
                          {})
    else:
        form = MyForm()
        return render(request,
                      'C:\\Users\\a.rusnak\\PycharmProjects\\AppColors\\AppPil\\color\\templates\\index.html',
                      {'form': form})


def ResView(request):
    text = request.session['num']
    request.session['num'] = ""
    return render(request,
                  'C:\\Users\\a.rusnak\\PycharmProjects\\AppColors\\AppPil\\color\\templates\\result.html',
                  {'text': text})


def black_and_white(f):
    image = Image.open(f)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    white, black = 0, 0
    factor = -100
    factor = ((255 + factor) // 2) * 3
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > factor:
                a, b, c = 255, 255, 255
                white += 1
            else:
                a, b, c = 0, 0, 0
                black += 1
            draw.point((i, j), (a, b, c))
    del draw
    return " ".join(["Всего белых: {0}, черных {1}, размерность: {2}/{3}".format(white, black,
                                                                                 str(width), str(height))])

