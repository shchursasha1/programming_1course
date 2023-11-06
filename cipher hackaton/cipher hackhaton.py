with open('Chorna_rada.txt', 'r', encoding='utf-8') as file:
    chorna_rada_text = file.read()

with open('Khiba_revut_voly.txt', 'r', encoding='utf-8') as file:
    khiba_revut_voly_text = file.read()

with open('Misto.txt', 'r', encoding='utf-8') as file:
    misto_text = file.read()

chorna_rada_lines = chorna_rada_text.splitlines()
khiba_revut_voly_lines = khiba_revut_voly_text.splitlines()
misto_lines = misto_text.splitlines()

chorna_rada_words = [line.split() for line in chorna_rada_lines]
khiba_revut_voly_words = [line.split() for line in khiba_revut_voly_lines]
misto_words = [line.split() for line in misto_lines]

for i in range(len(chorna_rada_words)):
    for j in range(len(chorna_rada_words[i])):
        chorna_rada_words[i][j] = ''.join(filter(str.isalnum, chorna_rada_words[i][j]))

for i in range(len(khiba_revut_voly_words)):
    for j in range(len(khiba_revut_voly_words[i])):
        khiba_revut_voly_words[i][j] = ''.join(filter(str.isalnum, khiba_revut_voly_words[i][j]))

for i in range(len(misto_words)):
    for j in range(len(misto_words[i])):
        misto_words[i][j] = ''.join(filter(str.isalnum, misto_words[i][j]))

chorna_rada_words = list(filter(None, chorna_rada_words))
misto_words = list(filter(None, misto_words))
khiba_revut_voly_words = list(filter(None, khiba_revut_voly_words))


pairs = [(154, 93), (1042, 16), (1095, 106), (760, 41), (1573, 14)]

for i, j in pairs:
    try:
        word_from_chorna_rada = chorna_rada_words[i - 1][j - 1]
        print(f'Chorna Rada: {word_from_chorna_rada}')
    except IndexError:
        print(f'Chorna Rada: IndexError')

    try:
        word_from_misto = misto_words[i - 1][j - 1]
        print(f'Misto: {word_from_misto}')
    except IndexError:
        print(f'Misto: IndexError')

    try:
        word_from_khiba_revut_voly = khiba_revut_voly_words[i - 1][j - 1]
        print(f'Khiba Revut Voly: {word_from_khiba_revut_voly}')
    except IndexError:
        print(f'Khiba Revut Voly: IndexError')