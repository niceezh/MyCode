import re


def grep(pattern: str, flags: str, files: list):
    flag_i = "-i" in flags
    flag_v = "-v" in flags
    flag_x = "-x" in flags
    flag_n = "-n" in flags
    flag_l = "-l" in flags
    multi_files = len(files) > 1

    if flag_x:
        pattern = f'^{pattern}$'
    reflags = re.IGNORECASE if flag_i else 0

    output = []
    matched_files = []

    for fname in files:
        with open(fname, 'r') as f:
            lines = f.readlines()

        for idx, line in enumerate(lines, 1):
            line = line.rstrip('\n')
            match_found = bool(re.search(pattern, line, reflags))

            if flag_v:
                match_found = not match_found

            if match_found:
                if flag_l:
                    matched_files.append(f'{fname}\n')
                    break

                parts = []
                if multi_files:
                    parts.append(fname)
                if flag_n:
                    parts.append(str(idx))
                parts.append(line)
                output.append(f"{':'.join(parts)}\n")

    if flag_l:
        return ''.join(matched_files)

    return ''.join(output)


if __name__ == '__main__':
    print(grep("WITH LOSS OF EDEN, TILL ONE GREATER MAN", "-n -i -x", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]))
