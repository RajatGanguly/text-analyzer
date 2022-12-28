# THIS FILE IS CREATED BY DEVELOPER
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    dj_text = request.POST.get("text", "Default")
    remove_punc = request.POST.get("remove_punc", "off")
    full_caps = request.POST.get("full_caps", "off")
    remove_newline = request.POST.get("remove_newline", "off")
    full_small = request.POST.get("full_small", "off")
    remove_extra_space = request.POST.get("remove_extra_space", "off")
    char_counter = request.POST.get("char_counter", "off")
    work = ""
    if remove_punc == "on":
        analyzed_text = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        for char in dj_text:
            if char not in punctuations:
                analyzed_text += char
        dj_text = analyzed_text
        work += "Remove Punctuations "

    if full_caps == "on":
        dj_text = dj_text.upper()
        work += "Upper Case "

    if full_small == "on":
        dj_text = dj_text.lower()
        work += "Lower Case "

    if remove_newline == "on":
        analyzed_text = ""
        for char in dj_text:
            if char != "\n" and char!="\r":
                analyzed_text += char
        dj_text = analyzed_text
        work += "New Line Remover "

    if remove_extra_space == "on":
        analyzed_text = ""
        dj_text = dj_text.strip()
        n = len(dj_text)
        for i in range(n-1):
            if dj_text[i] != " " or dj_text[i+1] != " ":
                analyzed_text += dj_text[i]
        work += "Xtra Space Remover "


    params = {"purpose": work, "analyzed_text": dj_text}

    if char_counter == "on":
        char_count = len(dj_text)
        work += "Character Count "
        params["count"] = char_count
    return render(request, "analyze.html", params)