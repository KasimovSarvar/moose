# from django.test import TestCase
#
# # Create your tests here.
# class Pagination:
#     def __init__(self, objects: list, per_page) -> None:
#         self.objects = objects
#         self.per_page = per_page
#         self.result = self.pagination()
#
#     def pagination(self):
#         r = []
#         for i in range(0, len(self.objects), self.per_page):
#             temp = []
#             for j in range(i, i + self.per_page):
#                 if j >= len(self.objects):
#                     break
#                 temp.append(self.objects[j])
#             r.append(temp)
#         return r
#
#     def get_page(self, page_number: int) -> list:
#         return self.result[page_number - 1]
#
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# per_page = 3
# paginator = Pagination(lst, per_page)
# print(paginator.result)
# print(paginator.get_page(3))
#
#
#
#
