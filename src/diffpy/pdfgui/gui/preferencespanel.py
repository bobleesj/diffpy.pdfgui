#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2007 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 16:05:32 2019

import wx
import wx.lib.filebrowsebutton
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui import tooltips
from diffpy.pdfgui.control import structureviewer

class PreferencesPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PreferencesPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizerPanelName = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_1.Add(sizerPanelName, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self.labelPanelName = wx.StaticText(self, wx.ID_ANY, "Preferences")
        self.labelPanelName.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Bitstream Vera Sans"))
        sizerPanelName.Add(self.labelPanelName, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        grid_sizer_1 = wx.GridSizer(3, 3, 10, 10)
        sizer_1.Add(grid_sizer_1, 0, wx.ALL, 5)

        self.labelViewer = wx.StaticText(self, wx.ID_ANY, "Structure viewer executable")
        grid_sizer_1.Add(self.labelViewer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)

        self.textCtrlViewer = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_1.Add(self.textCtrlViewer, 0, wx.EXPAND, 0)

        self.buttonViewerBrowse = wx.Button(self, wx.ID_ANY, "Browse")
        grid_sizer_1.Add(self.buttonViewerBrowse, 0, 0, 0)

        self.labelArgStr = wx.StaticText(self, wx.ID_ANY, "Argument string")
        grid_sizer_1.Add(self.labelArgStr, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)

        self.textCtrlArgument = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_1.Add(self.textCtrlArgument, 0, wx.EXPAND, 0)

        grid_sizer_1.Add((20, 20), 0, 0, 0)

        self.labelFormat = wx.StaticText(self, wx.ID_ANY, "Structure format")
        grid_sizer_1.Add(self.labelFormat, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)

        self.choiceFormat = wx.Choice(self, wx.ID_ANY, choices=[])
        grid_sizer_1.Add(self.choiceFormat, 0, wx.EXPAND, 0)

        grid_sizer_1.Add((20, 20), 0, 0, 0)

        self.structureDirCheckBox = wx.CheckBox(self, wx.ID_ANY, "Remember path to structure files")
        sizer_1.Add(self.structureDirCheckBox, 0, wx.ALL, 5)

        self.dataDirCheckBox = wx.CheckBox(self, wx.ID_ANY, "Remember path to data sets")
        sizer_1.Add(self.dataDirCheckBox, 0, wx.ALL, 5)

        sizer_1.Add((0, 0), 1, wx.EXPAND, 0)

        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)

        sizer_3.Add((0, 0), 1, 0, 0)

        self.okButton = wx.Button(self, wx.ID_OK, "OK")
        sizer_3.Add(self.okButton, 0, wx.ALL, 5)

        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        sizer_3.Add(self.cancelButton, 0, wx.ALL, 5)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onBrowse, self.buttonViewerBrowse)
        self.Bind(wx.EVT_BUTTON, self.onOK, self.okButton)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.cancelButton)
        # end wxGlade
        self.__customProperties()

    def __customProperties(self):
        """Set the custom properties."""

        # Fill the options in the format choice
        viewer = structureviewer.getStructureViewer()
        formats = viewer.getFileFormats()
        formats.sort()
        for fmt in formats:
            self.choiceFormat.Append(fmt)

        self.setToolTips(tooltips.preferencespanel)
        return


    def onCancel(self, event): # wxGlade: PreferencesPanel.<event_handler>
        """Cancel the changes. Go back to the last panel."""
        selections = self.treeCtrlMain.GetSelections()
        if selections:
            node = selections[0]
            entrytype = self.treeCtrlMain.GetNodeType(node)
        else:
            entrytype = None
        self.mainFrame.setMode("fitting")
        self.mainFrame.switchRightPanel(entrytype)
        return

    def onOK(self, event): # wxGlade: PreferencesPanel.<event_handler>
        """Record all of the preferences and return to fitting mode."""

        # Record structure viewer stuff
        executable = str(self.textCtrlViewer.GetValue()).strip()
        argstr = str(self.textCtrlArgument.GetValue()).strip()
        fileformat = str(self.choiceFormat.GetStringSelection())
        config = {
                "executable" : executable,
                "argstr"     : argstr,
                "fileformat" : fileformat,
                }

        viewer = structureviewer.getStructureViewer()
        viewer.setConfig(config)

        # Structures path
        remember = bool(self.structureDirCheckBox.GetValue())
        if not self.cP.has_section("PHASE"):
            self.cP.add_section("PHASE")
        self.cP.set("PHASE", "remember", str(remember))

        # Data set path
        remember = bool(self.dataDirCheckBox.GetValue())
        if not self.cP.has_section("DATASET"):
            self.cP.add_section("DATASET")
        self.cP.set("DATASET", "remember", str(remember))

        # Get out of here
        self.onCancel(event)
        return

    def refresh(self):
        """Refresh the panel."""

        # Structure viewer stuff
        viewer = structureviewer.getStructureViewer()
        config = viewer.getConfig()
        self.textCtrlViewer.SetValue(config["executable"])
        self.textCtrlArgument.SetValue(config["argstr"])
        self.choiceFormat.SetStringSelection(config["fileformat"])

        remember = False
        if self.cP.has_option("DATASET", "remember"):
            remember = self.cP.getboolean("DATASET", "remember")
        self.dataDirCheckBox.SetValue(remember)

        remember = False
        if self.cP.has_option("PHASE", "remember"):
            remember = self.cP.getboolean("PHASE", "remember")
        self.structureDirCheckBox.SetValue(remember)
        return

    def onBrowse(self, event): # wxGlade: PreferencesPanel.<event_handler>
        d = wx.FileDialog(None, "Choose structure viewer", ".", "",
                          "All Files|*", wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        if d.ShowModal() == wx.ID_OK:
            fullpath = d.GetPath()
            self.textCtrlViewer.SetValue(fullpath)
        return

# end of class PreferencesPanel
