from appJar import gui


mGui = gui("Demo", bg = "yellow")


def addmes():
    mGui.setMessage("msg", mGui.getMessage("msg") + "\n Hello pidor nah")


mGui.startScrollPane(title="pane", row=0,column = 0, rowspan=10,sticky="new")
mGui.addEmptyMessage("msg")
mGui.stopScrollPane()
mGui.addButton("msgB", addmes,10)
#mGui.startFrame("right", 1, 0, )
mGui.addLabel("lbl", "This is a label on red",11)
#mGui.stopFrame()
mGui.go()