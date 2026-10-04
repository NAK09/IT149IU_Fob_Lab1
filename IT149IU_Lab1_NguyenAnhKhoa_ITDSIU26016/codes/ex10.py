total_seconds = int(input("Enter a number of seconds (> 3600): "))

if total_seconds > 3600:
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60

    print(hours, minutes, seconds, sep=" - ")
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    check = (hours * 3600 + minutes * 60 + seconds) == total_seconds
    print("Verification:", check)
else:
    print("Error: Number of seconds must be greater than 3600")