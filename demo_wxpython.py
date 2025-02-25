import wx
# Création d'une application
app = wx.App(False)
# Création d'une fenêtre
frame = wx.Frame(None, wx.ID_ANY, "Ma première application wxPython", size=(300, 200))
# Ajout de widgets
panel = wx.Panel(frame, wx.ID_ANY)
text_ctrl = wx.TextCtrl(panel, wx.ID_ANY, "Bonjour, wxPython!", style=wx.TE_READONLY)
# Agencement des widgets
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
panel.SetSizer(sizer)
# Affichage de la fenêtre
frame.Show(True)
# Lancement de la boucle principale
app.MainLoop()