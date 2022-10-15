from django.http import HttpResponse


# <<<Exercise 2>>>

# def main(request):
#     return HttpResponse("MAIN VIEW!!")
#
# def url_articles(request):
#     return HttpResponse("You have reached the page: ARTICLES")
#
# def url_articles_archive(request):
#     return HttpResponse("You have reached the  child page Articles: ARCHIVE")
#
# def url_users(request):
#     return HttpResponse("You have reached the page: USERS")


# <<<Exercise 3>>>

def main(request):
    return HttpResponse("Hey! It's your main view!!")


def article_number(request, article_number):
    return HttpResponse(f"Page # {article_number}")


def article_number_arc(request, article_number):
    return HttpResponse(f"Page # {article_number} --- Archive")


def art_numb_slug(request, article_number, slug_text):
    return HttpResponse(f"Page # {article_number} / SLUG TEXT --- {slug_text}")


def user_number(request, user_numb=""):
    return HttpResponse(
        f"Если номер этой страницы возвести в квадрат то получим - {user_numb**2}" if user_numb else "Номер не введён")
    # Не пойму как сделать чтобы сработал ELSE!!!(

def regex(request, text):
    return HttpResponse(f"it's '{text}' from regexp")


def ua_number(request, numb):
    return HttpResponse(f"Введённый номер - {numb} - является корректным для территории УКРАИНЫ")

