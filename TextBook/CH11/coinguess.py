import random
guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください:')
    guess = input()
toss = random.randint(0, 1)
if (toss == 0 and guess == '裏') or (toss == 1 and guess == '表'):
    print('当たり')
else:
    print('ハズレ。もう一回遊べるドン')
    guess = input()
    if (toss == 0 and guess == '裏') or (toss == 1 and guess == '表'):
        print('当たり')
    else:
        print('ハズレ。このゲーム苦手ですね笑')
