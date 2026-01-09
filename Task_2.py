# TODO Найдите количество книг, которое можно разместить на дискете
DISK_SIZE_MB = 1.44
PAGES_PER_BOOK = 100
LINES_PER_PAGE = 50
CHARS_PER_LINE = 25
BYTES_PER_CHAR = 4

KB = 1024
MB = 1024 * KB

chars_per_book = PAGES_PER_BOOK * LINES_PER_PAGE * CHARS_PER_LINE
bytes_per_book = chars_per_book * BYTES_PER_CHAR

bytes_per_diskette = DISK_SIZE_MB * MB

books_per_diskette = int(bytes_per_diskette // bytes_per_book)

print("Количество книг, помещающихся на дискету:", books_per_diskette)