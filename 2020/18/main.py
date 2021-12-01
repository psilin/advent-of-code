
class Token:
    def __init__(self):
        self.children = []

    def add(self, t):
        self.children.append(t)

    def evaluate(self):
        val = 0
        op = None

        for ch in self.children:
            if ch == '+' or ch == '*':
                op = ch
            elif isinstance(ch, Token):
                if op == '+':
                    val += ch.evaluate()
                elif op == '*':
                    val *= ch.evaluate()
                else:
                    val = ch.evaluate()
            else:
                if op == '+':
                    val += ch
                elif op == '*':
                    val *= ch
                else:
                    val = ch
        return val

    def evaluate_adv(self):
        # doing +
        while '+' in self.children:
            val = 0
            for i in range(len(self.children)):
                if self.children[i] == '+':
                    t2 = self.children.pop(i + 1)
                    t1 = self.children.pop(i - 1)
                    for t in (t1, t2):
                        if isinstance(t, Token):
                            val += t.evaluate_adv()
                        else:
                            val += t
                    break
            self.children[i-1] = val 
        # doing *
        val = 1
        for ch in self.children:
            if isinstance(ch, Token):
                val *= ch.evaluate_adv()
            elif isinstance(ch, int):
                val *= ch
        return val
                
    def __repr__(self):
        mystr = '('
        for ch in self.children:
            mystr += ch.__repr__()
        mystr += ')'
        return mystr


def parse_input():
    data = []
    with open('./input.txt') as fh:
        for line in fh:
            line = line.strip('\n')
            cur = [Token(), ]
            for c in line:
                if c == '(':
                    cur.append(Token())
                elif c == ')':
                    t = cur.pop(-1)
                    cur[-1].add(t)
                elif c == '+' or c == '*':
                    cur[-1].add(c)
                elif c.isdigit() is True:
                    cur[-1].add(int(c))
            data.append(cur[-1])
    return data


if __name__ == '__main__':
    data = parse_input()
    d = [t.evaluate() for t in data]
    print(sum(d))
    dadv = [t.evaluate_adv() for t in data]
    print(sum(dadv))
