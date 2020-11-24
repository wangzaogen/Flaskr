

def offset_current(page_index: int, page_size: int):
    if page_index > 0:
        return (page_index - 1) * page_size
    else:
        return 0
