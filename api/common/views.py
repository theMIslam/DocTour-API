from api.common.mixins import GlobalSearchMixin
from drf_multiple_model.views import ObjectMultipleModelAPIView
from api.common.utils import LimitPagination



class GlobalSeacrh(ObjectMultipleModelAPIView, GlobalSearchMixin):
    """Global Searching in Multiple Models"""

    pagination_class = LimitPagination


    """/?search?={{ params }}"""

    def get_querylist(self):
        querylist = ()
        search = self.request.GET.get("search")

        if search:
            return self.global_querylist(querylist, search)
        return querylist
