def claim_doc_uploader(instance, filename):
    ''' Генератор пути файла '''

    file_type = filename.split('.')[-1]
    return f'claim-doc/{instance.pk}.{file_type}'