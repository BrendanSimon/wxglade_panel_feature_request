#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.0b1 on Tue Nov 13 20:52:30 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((903, 668))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        panel_4 = wx.Panel(self)
        panel_4.SetBackgroundColour(wx.Colour(219, 112, 219))
        #sizer_4 = wx.StaticBoxSizer(wx.StaticBox(panel_4, wx.ID_ANY, "Charlie"), wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        panel_4.SetSizer(sizer_4)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        panel_3 = wx.Panel(self)
        panel_3.SetBackgroundColour(wx.Colour(143, 188, 143))
        sizer_3a = wx.StaticBoxSizer(wx.StaticBox(panel_3, wx.ID_ANY, "Beta"), wx.HORIZONTAL)
        panel_3.SetSizer(sizer_3a)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Alpha"), wx.HORIZONTAL)
        sizer_2.Add((20, 20), 0, 0, 0)
        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("cat.png", wx.BITMAP_TYPE_ANY))
        bitmap_1.SetBackgroundColour(wx.Colour(255, 255, 0))
        sizer_2.Add(bitmap_1, 1, 0, 0)
        bitmap_2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("shield.png", wx.BITMAP_TYPE_ANY))
        bitmap_2.SetBackgroundColour(wx.Colour(255, 255, 0))
        sizer_2.Add(bitmap_2, 1, 0, 0)
        bitmap_3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("bulb.png", wx.BITMAP_TYPE_ANY))
        bitmap_3.SetBackgroundColour(wx.Colour(255, 255, 0))
        sizer_2.Add(bitmap_3, 1, 0, 0)
        sizer_2.Add((20, 20), 1, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 10)
        sizer_3a.Add((20, 20), 1, 0, 0)
        bitmap_4 = wx.StaticBitmap(panel_3, wx.ID_ANY, wx.Bitmap("heart.png", wx.BITMAP_TYPE_ANY))
        sizer_3a.Add(bitmap_4, 1, 0, 0)
        bitmap_5 = wx.StaticBitmap(panel_3, wx.ID_ANY, wx.Bitmap("add.png", wx.BITMAP_TYPE_ANY))
        sizer_3a.Add(bitmap_5, 1, 0, 0)
        bitmap_6 = wx.StaticBitmap(panel_3, wx.ID_ANY, wx.Bitmap("error.png", wx.BITMAP_TYPE_ANY))
        sizer_3a.Add(bitmap_6, 1, 0, 0)
        sizer_3a.Add((20, 20), 1, 0, 0)
        sizer_3.Add(panel_3, 1, wx.ALL | wx.EXPAND, 10)
        sizer_1.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 10)
        sizer_4.Add((20, 20), 1, 0, 0)
        bitmap_7 = wx.StaticBitmap(panel_4, wx.ID_ANY, wx.Bitmap("check.png", wx.BITMAP_TYPE_ANY))
        sizer_4.Add(bitmap_7, 1, 0, 0)
        bitmap_8 = wx.StaticBitmap(panel_4, wx.ID_ANY, wx.Bitmap("star.png", wx.BITMAP_TYPE_ANY))
        sizer_4.Add(bitmap_8, 1, 0, 0)
        bitmap_9 = wx.StaticBitmap(panel_4, wx.ID_ANY, wx.Bitmap("map.png", wx.BITMAP_TYPE_ANY))
        sizer_4.Add(bitmap_9, 1, 0, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        #sizer_1.Add(sizer_4, 1, wx.ALL | wx.EXPAND, 10)
        sizer_1.Add(panel_4, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
