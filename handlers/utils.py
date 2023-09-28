from datetime import date


def to_date(date_str: str) -> date | None:
    try:
        day, month, year = date_str.split(".")
        res_date = date(day=int(day), month=int(month), year=int(year))
        return res_date
    except Exception:
        return None
