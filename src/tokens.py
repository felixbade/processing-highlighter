groups = 'NULL COMMENT1 COMMENT2 LITERAL1 LITERAL2 LABEL KEYWORD1 KEYWORD2 KEYWORD3 KEYWORD4 KEYWORD5 KEYWORD6 FUNCTION1 FUNCTION2 FUNCTION3 FUNCTION4 OPERATOR INVALID'.split()

for line in open('keywords.txt'):
    line = line.replace('\n', '')

    words = line.split()
    
    if len(words) < 2:
        continue

    group = words[1]
    if group not in groups:
        continue

    token = words[0]
    print('"%s": "%s",' % (token, group.lower()))
    #print(token, group.lower())
