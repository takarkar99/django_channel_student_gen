# from django.shortcuts import render
# import yfinance as yf


# def code(request):
#     temp = 'Home/Home.html'
#     stock = yf.Ticker('AAPL')
#     data = stock.history(period="1d")
#     stock = data.to_dict()
#     # d2 = d1.values()
#     # for i in d2.values():
#     #     print(i)
#     li = []
#     l = ["open","high","low","close"]
#     d = {}
#     for i in stock.values():
#         for j in i.values():
#             li.append(j)
#     for i, j in zip(l,li):
#         d[i] = j
#     print(d)
#     context = {'stock': d}
#     return render(request, temp, context)