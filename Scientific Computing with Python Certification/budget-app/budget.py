class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, desc=''):
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount, desc=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': desc})
            return True
        else:
            return False

    def get_balance(self):
        balance = [dic['amount'] for dic in self.ledger]
        balance = sum(balance)
        return balance

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, desc=f'Transfer to {other.category}')
            other.deposit(amount, desc=f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        lines = ['{:*^30}'.format(f'{self.category}')]
        for item in self.ledger:
            if len(item['description']) > 23:
                desc = item['description'][:23]
            else:
                desc = item['description']
            lines.append(desc.ljust(23) + str("{:.2f}".format(item['amount'])).rjust(7))
        lines.append(f"Total: {self.get_balance()}")
        return '\n'.join(lines)


def create_spend_chart(categories):
    lines = ['Percentage spent by category']
    spends = []
    for cat in categories:
        temp = 0
        for dic in cat.ledger:
            if dic['amount'] < 0:
                temp = temp + dic['amount']
        spends.append(-temp)
    total = sum(spends)
    perc = [(spend / total * 100) for spend in spends]
    perc = [(num - (num % 10)) // 10 for num in perc]
    hist = ['    ' + '-' * ((len(categories) * 3) + 1)]
    bars = []
    for n in perc:
        bars.append(['o' if i <= n else ' ' for i in range(11)])
    numbers = [str(x * 10).rjust(3) + '|' for x in range(11)]
    bars.insert(0, numbers)
    bars.append(['' for _ in range(11)])
    for i in zip(*bars):
        temp = []
        for j in range(len(bars)):
            temp.append(i[j])
            t1 = [' '.join(temp[:2])]
            t1.extend(temp[2:])
        hist.insert(0, '  '.join(t1))
    lines.extend(hist)
    names = [list(self.category) for self in categories]
    name_bars = []
    length = max([len(name) for name in names])
    for name in names:
        name_bars.append([name[x] if x < len(name) else ' ' for x in range(length)])
    name_bars.insert(0, ['    ' for _ in range(length)])
    name_bars.append(['' for _ in range(length)])
    for i in zip(*name_bars):
        temp = []
        for j in range(len(name_bars)):
            temp.append(i[j])
            t1 = [' '.join(temp[:2])]
            t1.extend(temp[2:])
        lines.append('  '.join(t1))
    return '\n'.join(lines)
