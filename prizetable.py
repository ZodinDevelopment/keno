from settings import PRIZES


class PrizeTable:
    def __init__(self, picks, bet=1):
        self.picks = len(picks)
        self.bet = bet
        # Should be a dictionary returned by PRIZES.get(picks)
        self._table = PRIZES.get(self.picks)

    def win(self, hits):
        won = self._table.get(hits)
        if won is None:
            return 0
        else:
            return won * self.bet

    def __str__(self):
        if self._table is None:
            return f"0 MARKED\n{'='*8}\nBET {self.bet}"
        else:

            table_str = [
                f"{self.picks} MARKED",
                f"{'='*8}",
                "HIT / WON",
            ]

            for pick in self._table.keys():
                lin = f" {pick} : {self._table[pick]*self.bet}"
                table_str.append(lin)

            final = f"BET {self.bet}"
            table_str.append(final)
            table_str = "\n".join(table_str)

            return table_str



