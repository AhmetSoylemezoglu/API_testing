# I will use a api to check language of a given text. Maybe a basic GUI with tkinter
import detectlanguage

my_key = "6c8b289b01a6edfe12d37e00771ff089"

detectlanguage.configuration.api_key = my_key

print(detectlanguage.account_status())