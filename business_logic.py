from datetime import datetime, timedelta

SA_PUBLIC_HOLIDAYS = {
    "2025-01-01", "2025-03-21", "2025-04-18", "2025-04-21", "2025-04-27",
    "2025-05-01", "2025-06-16", "2025-08-09", "2025-09-24", "2025-12-16",
    "2025-12-25", "2025-12-26"
}

WORK_START = 8  # 08:00
WORK_END = 17  # 17:00

def is_business_day(date: datetime) -> bool:
    return date.weekday() < 5 and date.strftime("%Y-%m-%d") not in SA_PUBLIC_HOLIDAYS

def calculate_business_seconds(start: datetime, end: datetime) -> int:
    total_seconds = 0
    current = start

    while current < end:
        if is_business_day(current):
            work_start = current.replace(hour=WORK_START, minute=0, second=0, microsecond=0)
            work_end = current.replace(hour=WORK_END, minute=0, second=0, microsecond=0)

            if current < work_start:
                current = work_start
            elif current >= work_end:
                current = (current + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
                continue

            second_end = min(end, work_end)
            total_seconds += int((second_end - current).total_seconds())
            current = second_end
        else:
            current = (current + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

    return total_seconds
