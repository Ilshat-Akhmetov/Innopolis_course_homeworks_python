def check_happy_ticket(ticket: str) -> str:
    n = len(ticket)
    first_half_s = sum(int(ch) for ch in ticket[:n//2])
    second_half_s = sum(int(ch) for ch in ticket[n//2:])
    if first_half_s == second_half_s:
        return "Счастливый"
    return "Обычный"

def test_1():
    ticket = "090234"
    ans = check_happy_ticket(ticket)
    assert ans == "Счастливый"

def test_2():
    ticket = "123456"
    ans = check_happy_ticket(ticket)
    assert ans == "Обычный"

def output_check_ticket(ticket: str) -> None:
    print(check_happy_ticket(ticket))

ticket = "090234"
output_check_ticket(ticket)

ticket = "123456"
output_check_ticket(ticket)

