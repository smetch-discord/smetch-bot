from dateutil.relativedelta import relativedelta


def _stringify_time_unit(unit, value) -> str:
    '''
    Returns a string representing a certain unit of time.
    For example:
    >>> _stringify_time_unit('hours', 9)
    '9 hours'
    >>> _stringify_time_unit('minutes', 0)
    'less than a minute'
    '''
    if unit == 'seconds' and value == 0:
        return '0 seconds'
    elif value == 1:
        # Use singular noun if there is only 1 unit
        return f'{value} {unit[:-1]}'
    elif value == 0:
        # Use 'less than a' if there are 0 units
        return f'less than a {unit[:-1]}'
    else:
        return f'{value} {unit}'


def humanize_delta(delta: relativedelta, precision: str = 'seconds', max_units: int = 6) -> str:
    '''
    Returns a human-readable version of the `relativedelta` object.
    `precision` specifies the smallest unit of time to include (e.g. 'seconds', 'minutes').
    `max_units` specifies the maximum number of units of time to include (e.g. 1 may include days but not hours).
    '''
    if max_units <= 0:
        raise ValueError('max_units must be positive')

    units: tuple[tuple[str, int]] = (
        ('years', delta.years),
        ('months', delta.months),
        ('days', delta.days),
        ('hours', delta.hours),
        ('minutes', delta.minutes),
        ('seconds', delta.seconds),
    )

    # Add the time units that are greater than 0, but stop at accuracy or max_units.
    time_strings: list[str] = []
    unit_count: int = 0

    for unit, value in units:
        if value:
            time_strings.append(_stringify_time_unit(unit, value))
            unit_count += 1

        if unit == precision or unit_count >= max_units:
            break

    # Add the 'and' between the last two units, if necessary
    if len(time_strings) > 1:
        time_strings[-1] = f'{time_strings[-2]} and {time_strings[-1]}'
        del time_strings[-2]

    # If nothing has been found, just make the value 0 units of `precision`, e.g. `0 days`.
    if not time_strings:
        humanized: str = _stringify_time_unit(0, precision)
    else:
        humanized: str = ', '.join(time_strings)

    return humanized
