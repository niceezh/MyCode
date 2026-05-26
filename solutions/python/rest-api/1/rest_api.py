import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database or {'users': []}

    def get(self, url, payload=None):
        if url == '/users':
            users = self.database['users']

            if payload:
                data = json.loads(payload)
                requested_names = data.get('users', [])
                filtered_users = [u for u in users if u['name'] in requested_names]
                filtered_users.sort(key=lambda x: x['name'])
                return json.dumps({'users': filtered_users})

            all_users = sorted(users, key=lambda x: x['name'])
            return json.dumps({'users': all_users})

        return json.dumps({})

    def post(self, url, payload=None):
        if not payload:
            return json.dumps({})

        data = json.loads(payload)

        if url == '/add':
            return self._add_user(data)
        elif url == '/iou':
            return self._handle_iou(data)

        return json.dumps({})

    def _add_user(self, data):
        name = data['user']
        new_user = {
            'name': name,
            'owes': {},
            'owed_by': {},
            'balance': 0.0
        }
        self.database['users'].append(new_user)
        return json.dumps(new_user)

    def _handle_iou(self, data):
        lender_name = data['lender']
        borrower_name = data['borrower']
        amount = data['amount']

        lender = None
        borrower = None

        for user in self.database['users']:
            if user['name'] == lender_name:
                lender = user
            elif user['name'] == borrower_name:
                borrower = user

        if not lender or not borrower:
            return json.dumps({'error': 'User not found'})

        debt_from_lender_to_borrower = lender['owes'].get(borrower_name, 0.0)

        if debt_from_lender_to_borrower > 0:
            if amount < debt_from_lender_to_borrower:
                reduction = amount

                lender['owes'][borrower_name] -= reduction
                borrower['owed_by'][lender_name] -= reduction

                lender['balance'] += reduction
                borrower['balance'] -= reduction

            else:
                old_debt = debt_from_lender_to_borrower

                del lender['owes'][borrower_name]
                if lender_name in borrower['owed_by']:
                    del borrower['owed_by'][lender_name]

                lender['balance'] += old_debt
                borrower['balance'] -= old_debt

                remaining_amount = amount - old_debt

                if remaining_amount > 0:
                    self._add_debt(borrower, lender, remaining_amount)

        else:
            self._add_debt(borrower, lender, amount)

        result_users = [lender, borrower]
        result_users.sort(key=lambda x: x['name'])

        return json.dumps({'users': result_users})

    def _add_debt(self, debtor, creditor, amount):
        if amount <= 0:
            return

        debtor_name = debtor['name']
        creditor_name = creditor['name']

        current_owe = debtor['owes'].get(creditor_name, 0.0)
        debtor['owes'][creditor_name] = current_owe + amount

        current_owed_by = creditor['owed_by'].get(debtor_name, 0.0)
        creditor['owed_by'][debtor_name] = current_owed_by + amount

        debtor['balance'] -= amount
        creditor['balance'] += amount
