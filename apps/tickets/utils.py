import os


def get_filename_ext(filepath):
    """Return a basename from a filepath"""
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)


def upload_file_path(instance, filename):
    """Return upload path"""
    name, ext = get_filename_ext(filename)
    new_filename = hash(name)
    ticket_pk = instance.ticket.pk
    return f'files/{ticket_pk}/{ticket_pk}-{new_filename}{ext}'
