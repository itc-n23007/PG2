import pyinputplus as pyip

prices = {
    'bread': {'小麦パン': 220, '白パン': 220, 'サワー種': 230},
    'protein': {'チキン': 230, 'ターキー': 200, 'ハム': 100, '豆腐': 100},
    'cheese': {'チェダー': 190, 'スイス': 130, 'モツァレラ': 180},
    'extras': {'マヨネーズ': 28, 'からし': 20, 'レタス': 30, 'トマト': 30}
}

bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt="パンの種類を選んでください:\n")
protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt="タンパク質の種類を選んでください:\n")
cheese = pyip.inputYesNo("チーズが必要ですか? (yes/no): ")

cheese = None
if cheese == 'yes':
    cheese = pyip.inputMenu(['チェダー', 'スイス', 'モツァレラ'], prompt="チーズの種類を選んでください:\n")

extras = {}
for extra in ['マヨネーズ', 'からし', 'レタス', 'トマト']:
    response = pyip.inputYesNo(f"{extra}が必要ですか? (yes/no): ")
    if response == 'yes':
        extras[extra] = True
    else:
        extras[extra] = False

sandwiches = pyip.inputInt("サンドイッチはいくつ必要ですか? (1以上): ", min=1)

total_cost = 0
total_cost += prices['bread'][bread]
total_cost += prices['protein'][protein]
if cheese:
    total_cost += prices['cheese'][cheese]
for extra in extras:
    if extras[extra]:
        total_cost += prices['extras'][extra]

total_cost *= sandwiches

print(f"\nサンドイッチの合計金額は: ¥{total_cost:} です。")
