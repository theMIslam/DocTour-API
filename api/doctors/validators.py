# from django.utils.regex_helper import _lazy_re_compile
# from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError
# from django.utils.deconstruct import deconstructible


# @deconstructible
# class DoubleRegexValidator:
#     regex = ""
#     regex2 = ""
#     message = _("Enter a valid value.")
#     code = "invalid"
#     inverse_match = False
#     flags = 0

#     def __init__(
#         self,
#         regex=None,
#         regex2=None,
#         message=None,
#         code=None,
#         inverse_match=None,
#         flags=None,
#     ):
#         if regex is not None:
#             self.regex = regex
#         if regex2 is not None:
#             self.regex2 = regex2
#         if message is not None:
#             self.message = message
#         if code is not None:
#             self.code = code
#         if inverse_match is not None:
#             self.inverse_match = inverse_match
#         if flags is not None:
#             self.flags = flags
#         if self.flags and not isinstance(self.regex, str):
#             raise TypeError(
#                 "If the flags are set, regex must be a regular expression string."
#             )

#         self.regex = _lazy_re_compile(self.regex, self.flags)
#         self.regex2 = _lazy_re_compile(self.regex2, self.flags)

#     def __call__(self, value):
#         """
#         Validate that the input contains (or does *not* contain, if
#         inverse_match is True) a match for the regular expression.
#         """
#         regex_matches = self.regex.search(str(value))
#         invalid_input = regex_matches if self.inverse_match else not regex_matches
#         if invalid_input:
#             regex_matches2 = self.regex2.search(str(value))
#             invalid_input2 = (
#                 regex_matches2 if self.inverse_match else not regex_matches2
#             )
#             if invalid_input2:
#                 raise ValidationError(
#                     self.message, code=self.code, params={"value": value}
#                 )

#     def __eq__(self, other):
#         return (
#             isinstance(other, DoubleRegexValidator)
#             and self.regex.pattern == other.regex.pattern
#             and self.regex2.pattern == other.regex.pattern
#             and self.regex.flags == other.regex.flags
#             and (self.message == other.message)
#             and (self.code == other.code)
#             and (self.inverse_match == other.inverse_match)
#         )


# PhoneValidator = DoubleRegexValidator(
#     regex=r"^996(\d{3})\d{2}\d{2}\d{2}$", regex2=r"^312\d{2}\d{2}\d{2}$"
# )

from django.core.validators import RegexValidator
PhoneValidator = RegexValidator(regex=r"^996(\d{3})\d{2}\d{2}\d{2}$")