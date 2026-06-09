CANONICAL = {

    "gps": "POSITION",
    "irs": "POSITION",
    "position": "POSITION",

    "track": "LNAV",
    "cross-track": "LNAV",

    "tod": "VNAV",
    "toc": "VNAV",

    "fuel": "FUEL",

    "display": "DISPLAY",

    "alert": "ALERT",

    "fault": "HEALTH",

    "maintenance": "HEALTH"
}

def normalize(items):

    normalized = []

    for item in items:

        lower = item.lower()

        matched = False

        for key, value in CANONICAL.items():

            if key in lower:

                normalized.append(value)
                matched = True

                break

        if not matched:
            normalized.append(item.upper())

    return list(set(normalized))