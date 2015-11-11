#-*-coding:utf8-*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect,RequestContext
from django.views.decorators.csrf import csrf_exempt
import json

def addspace(request):
    return render_to_response("addspace.html")

def is_chinese(uchar):
    # 判断一个unicode是否是汉字
    if uchar>= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False

def is_english(uchar):
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def is_erightbracket(uchar):
    if uchar==u')':
        return True
    else:
        return False

def is_crightbracket(uchar):
    if uchar==u'\uff09':
        return True
    else:
        return False

def checkText(teststring):
    addpositions = []
    newstring = ""
    testlist = list(teststring)
    for i in range(0,len(testlist)):
        if i<len(testlist)-1:
            if (is_chinese(testlist[i]) and is_number(testlist[i+1])) or (is_chinese(testlist[i]) and is_english(testlist[i+1])):
                testlist[i] = testlist[i]+" "
                addpositions.append(i)
            elif (is_number(teststring[i]) and is_chinese(teststring[i+1])):
                testlist[i] = testlist[i]+" "
                addpositions.append(i)
            elif (is_english(teststring[i]) and is_chinese(teststring[i+1])):
                testlist[i] = testlist[i]+" "
                addpositions.append(i)
            elif (is_erightbracket(teststring[i]) and is_chinese(teststring[i+1])):
                testlist[i] = testlist[i]+" "
                addpositions.append(i)
            elif (is_crightbracket(teststring[i]) and is_number(teststring[i+1])) or (is_crightbracket(teststring[i]) and is_english(teststring[i+1])):
                testlist[i] = testlist[i]+" "
                addpositions.append(i)

        newstring = newstring+testlist[i]

    result = [newstring,addpositions]
    return result

@csrf_exempt
def convert(request):
    testText = request.POST.get('teststring')
    newstring = checkText(testText)[0]
    addpositions = checkText(testText)[1]
    result = {}
    result['data'] = newstring
    result['position'] = addpositions
    return HttpResponse(json.dumps(result),content_type="application/json")

