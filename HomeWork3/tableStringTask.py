# кузнецов Rлексей DdD
x = 'кузнецов'
y = 'Rлексей'
z = 'DdD'
x = x.capitalize()
y = y.replace('R', 'А', 1)
z = z.replace('DdD', 'Сергеевич')
print(x, y, z)


full_name = " кузнецов Rлексей DdD"
print(full_name.strip().lower().replace('r', 'А').replace('ddd', 'Сергеевич').title())
