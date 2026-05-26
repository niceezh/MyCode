import re


def parse(markdown):

    lines = markdown.split('\n')
    result = []
    in_list = False

    HEADINGS = [
        (re.compile(r'###### (.*)'), 'h6'),
        (re.compile(r'##### (.*)'), 'h5'),
        (re.compile(r'#### (.*)'), 'h4'),
        (re.compile(r'### (.*)'), 'h3'),
        (re.compile(r'## (.*)'), 'h2'),
        (re.compile(r'# (.*)'), 'h1'),
    ]

    for line in lines:

        for pattern, tag in HEADINGS:
            match = pattern.fullmatch(line)
            if match:
                line = f'<{tag}>{match.group(1)}</{tag}>'
                break

        match = re.fullmatch(r'\* (.*)', line)
        if match:
            content = match.group(1)
            if in_list:
                line = f'<li>{content}</li>'
            else:
                line = f'<ul><li>{content}</li>'
                in_list = True
        else:
            if in_list:
                result.append('</ul>')
                in_list = False

        if not re.match(r'<h|<ul|<li', line):
            line = f'<p>{line}</p>'

        match = re.match(r'(.*)__(.*)__(.*)', line)
        if match:
            line = f'{match.group(1)}<strong>{match.group(2)}</strong>{match.group(3)}'

        match = re.match(r'(.*)_(.*)_(.*)', line)
        if match:
            line = f'{match.group(1)}<em>{match.group(2)}</em>{match.group(3)}'

        result.append(line)

    if in_list:
        result.append('</ul>')

    return ''.join(result)
