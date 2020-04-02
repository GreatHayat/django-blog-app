from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    if filesize > 2000000:
        raise ValidationError(f"The maximum file size that can be uploaded is 2 MB")
    else:
        return value
