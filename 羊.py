def sheep(x,y):
    request_header = {"t":x}
    for i in range(y):
        requests.get("http://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=15&rank_role=1&skin=1", headers=request_header)
        print('第{}次通关'.format(i))
    print('success!!')
x=input('输入token:')
y=int(input('输入次数:'))
sheep(x,y)