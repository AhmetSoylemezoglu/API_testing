#nicegui modülünü deneyecem
from nicegui import ui

def chng():
    a.text+="yazı değişti"


ui.page_title("benim sitem")
a = ui.label("merhaba dünya 2")
ui.label("2. yazı bu da")



ui.button("bana bas", on_click=chng)









ui.run()