class Invoice:
    def __init__(self, client, total, type):
        self.client = client
        self.total = total
        self.type = type

    def __str__(self):
        return f'Invoice from {self.client} for {self.total} {self.type}'


inv = Invoice('Google', 500, 'dollars')
print(str(inv))