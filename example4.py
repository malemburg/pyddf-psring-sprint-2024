from taipy import Gui

# Add a navbar to switch from one page to the other
root_md = "<|navbar|>"
page1_md = "## This is page 1"
page2_md = "## This is page 2"

pages = {
    "/": root_md,
    "page1": page1_md,
    "page2": page2_md
}
Gui(pages=pages).run()
