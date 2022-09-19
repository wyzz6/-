import requests
import tkinter
import tkinter.messagebox
import fake_useragent
window = tkinter.Tk()
window.title('羊')
window.geometry('185x120')
def game(x,y):
    url="https://api.cprk.cc/ylgy?uid="+x
    ret = requests.get(url)
    t=ret.json()["data"]
    request_header = {"t":t,
    'UserAgent':fake_useragent.UserAgent().chrome}
    for i in range(y):
        requests.get("http://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=15&rank_role=1&skin=1", headers=request_header)
        print('第{}次通关'.format(i+1))
    print('success!!')
text1=tkinter.Label(window,text='uid:')
text1.place(x=1,y=30)
entry1 = tkinter.Entry(window,width=15)
entry1.place(x=39,y=30)
text2=tkinter.Label(window,text='次数:')
text2.place(x=1,y=60)
entry2 = tkinter.Entry(window,width=10)
entry2.place(x=39,y=60)
button = tkinter.Button(window,width=8,height=1,command=lambda:game(entry1.get(),int(entry2.get())),text='开刷')
button.place(x=40,y=85)
window.mainloop() 