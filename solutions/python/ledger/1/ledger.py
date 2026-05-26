from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = datetime(1970, 1, 1)
        self.description = ''
        self.change = 0


def create_entry(date: str, description: str, change: int):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency: str, locale: str, entries: list):
    if entries is None:
        return ''

    entries.sort(key=lambda entry: (entry.date, entry.change, entry.description))

    if locale == 'en_US':
        table = ['Date       | Description               | Change       ']
        for entry in entries:
            date_str = datetime.strftime(entry.date, '%m/%d/%Y')
            description_str = f'{entry.description[:22]}...' if len(entry.description) > 25 else str.ljust(entry.description, 25)
            change_symbol = '$' if currency == 'USD' else '€' if currency == 'EUR' else ''
            change_value = f'{abs(entry.change) / 100.0:,.2f}'
            change_str = f'({change_symbol}{change_value})'.rjust(13) if entry.change < 0 else f'{change_symbol}{change_value} '.rjust(13)
            table.append(f'{date_str} | {description_str} | {change_str}')
        return '\n'.join(table)

    if locale == 'nl_NL':
        table = ['Datum      | Omschrijving              | Verandering  ']
        for entry in entries:
            date_str = datetime.strftime(entry.date, '%d-%m-%Y')
            description_str = f'{entry.description[:22]}...' if len(entry.description) > 25 else str.ljust(entry.description, 25)
            change_symbol = '$' if currency == 'USD' else '€' if currency == 'EUR' else ''
            change_value = f'{entry.change / 100.0:,.2f}'
            change_value_modify = ''
            for char in change_value:
                if char == '.':
                    change_value_modify += ','
                    continue
                if char == ',':
                    change_value_modify += '.'
                    continue
                change_value_modify += char
            change_str = f'{change_symbol} {change_value_modify} '.rjust(13)
            table.append(f'{date_str} | {description_str} | {change_str}')
        return '\n'.join(table)

    return ''
