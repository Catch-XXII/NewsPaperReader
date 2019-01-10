import webbrowser
import codecs
filename = '.../news.txt'
path_to_browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
url = list()
name = list()
with codecs.open(filename, 'r', encoding='utf8') as f:
    next(f)
    print('{:>15s}{:>15s}{:>15s}{:>30s}'.format('Name', 'Frequency', 'Circulation', 'Web-site'))
    for row in f:
        rows = row.split()
        print('{:>15s}{:>15s}{:>15s}{:>30s}'.format(rows[0], rows[1], rows[2], rows[3]))
        url.append(rows[3])
        name.append(rows[0])
selection = input('\nLütfen bir gazete seçiniz: ').capitalize()
for i in range(len(name)):
    if selection == name[i]:
        print('Seçtiğiniz gazete: ', name[i])
        webbrowser.get(path_to_browser).open(url[i])
