class Service:
    model = None

    @classmethod
    def get(cls, *args, **kwargs):
        try:
            return cls.model.objects.get(*args, **kwargs)
        except cls.model.DoesNotExist:
            raise ValueError('Model have to be instant')

    @classmethod
    def filter(cls, *args, **kwargs):
        try:
            return cls.model.objects.filter(*args, **kwargs).order_by('-created_at')
        except cls.model.DoesNotExist:
            raise ValueError('Model have to be instant')
