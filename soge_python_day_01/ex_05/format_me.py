def format_me(date, format):
    def format_date():
        return date.strftime(format)
    return format_date()