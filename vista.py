# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class to_do
###########################################################################

class to_do ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1018,589 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		main = wx.BoxSizer( wx.VERTICAL )

		nomain = wx.BoxSizer( wx.HORIZONTAL )

		todosizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"To-Do", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		todosizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.panel_to_do = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		aSizer = wx.BoxSizer( wx.VERTICAL )

		self.a_Panel1 = wx.Panel( self.panel_to_do, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		aSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self.a_Panel1, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		aSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.a_Panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		aSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.a_Panel1, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button2.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		aSizer1.Add( self.m_button2, 0, wx.ALL, 5 )


		self.a_Panel1.SetSizer( aSizer1 )
		self.a_Panel1.Layout()
		aSizer1.Fit( self.a_Panel1 )
		aSizer.Add( self.a_Panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.a_Panel2 = wx.Panel( self.panel_to_do, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		aSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self.a_Panel2, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		aSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.a_Panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		aSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self.a_Panel2, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button4.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		aSizer2.Add( self.m_button4, 0, wx.ALL, 5 )


		self.a_Panel2.SetSizer( aSizer2 )
		self.a_Panel2.Layout()
		aSizer2.Fit( self.a_Panel2 )
		aSizer.Add( self.a_Panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.a_Panel3 = wx.Panel( self.panel_to_do, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		aSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5 = wx.Button( self.a_Panel3, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		aSizer3.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.a_Panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		aSizer3.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self.a_Panel3, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button6.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		aSizer3.Add( self.m_button6, 0, wx.ALL, 5 )


		self.a_Panel3.SetSizer( aSizer3 )
		self.a_Panel3.Layout()
		aSizer3.Fit( self.a_Panel3 )
		aSizer.Add( self.a_Panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.a_Panel4 = wx.Panel( self.panel_to_do, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		aSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button7 = wx.Button( self.a_Panel4, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		aSizer4.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.a_Panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		aSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self.a_Panel4, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		aSizer4.Add( self.m_button8, 0, wx.ALL, 5 )


		self.a_Panel4.SetSizer( aSizer4 )
		self.a_Panel4.Layout()
		aSizer4.Fit( self.a_Panel4 )
		aSizer.Add( self.a_Panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.a_Panel4 = wx.Panel( self.panel_to_do, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		aSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button9 = wx.Button( self.a_Panel4, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		aSizer5.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.a_Panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		aSizer5.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.a_Panel4, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button10.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		aSizer5.Add( self.m_button10, 0, wx.ALL, 5 )


		self.a_Panel4.SetSizer( aSizer5 )
		self.a_Panel4.Layout()
		aSizer5.Fit( self.a_Panel4 )
		aSizer.Add( self.a_Panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_to_do.SetSizer( aSizer )
		self.panel_to_do.Layout()
		aSizer.Fit( self.panel_to_do )
		todosizer.Add( self.panel_to_do, 1, wx.EXPAND |wx.ALL, 5 )


		nomain.Add( todosizer, 1, wx.EXPAND, 5 )

		incoursesizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"In Course", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		incoursesizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.panel_incourse = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.b_Panel1 = wx.Panel( self.panel_incourse, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button11 = wx.Button( self.b_Panel1, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer1.Add( self.m_button11, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.b_Panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer1.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_button12 = wx.Button( self.b_Panel1, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer1.Add( self.m_button12, 0, wx.ALL, 5 )


		self.b_Panel1.SetSizer( bSizer1 )
		self.b_Panel1.Layout()
		bSizer1.Fit( self.b_Panel1 )
		bSizer.Add( self.b_Panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.b_Panel2 = wx.Panel( self.panel_incourse, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button13 = wx.Button( self.b_Panel2, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button13.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer2.Add( self.m_button13, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.b_Panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer2.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_button14 = wx.Button( self.b_Panel2, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button14.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer2.Add( self.m_button14, 0, wx.ALL, 5 )


		self.b_Panel2.SetSizer( bSizer2 )
		self.b_Panel2.Layout()
		bSizer2.Fit( self.b_Panel2 )
		bSizer.Add( self.b_Panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.b_Panel3 = wx.Panel( self.panel_incourse, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button15 = wx.Button( self.b_Panel3, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button15.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer3.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.b_Panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer3.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self.b_Panel3, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button16.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer3.Add( self.m_button16, 0, wx.ALL, 5 )


		self.b_Panel3.SetSizer( bSizer3 )
		self.b_Panel3.Layout()
		bSizer3.Fit( self.b_Panel3 )
		bSizer.Add( self.b_Panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.b_Panel4 = wx.Panel( self.panel_incourse, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button17 = wx.Button( self.b_Panel4, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button17.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer4.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.b_Panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer4.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self.b_Panel4, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button18.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer4.Add( self.m_button18, 0, wx.ALL, 5 )


		self.b_Panel4.SetSizer( bSizer4 )
		self.b_Panel4.Layout()
		bSizer4.Fit( self.b_Panel4 )
		bSizer.Add( self.b_Panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.b_Panel5 = wx.Panel( self.panel_incourse, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button19 = wx.Button( self.b_Panel5, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button19.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer5.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.b_Panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer5.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self.b_Panel5, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer5.Add( self.m_button20, 0, wx.ALL, 5 )


		self.b_Panel5.SetSizer( bSizer5 )
		self.b_Panel5.Layout()
		bSizer5.Fit( self.b_Panel5 )
		bSizer.Add( self.b_Panel5, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_incourse.SetSizer( bSizer )
		self.panel_incourse.Layout()
		bSizer.Fit( self.panel_incourse )
		incoursesizer.Add( self.panel_incourse, 1, wx.EXPAND |wx.ALL, 5 )


		nomain.Add( incoursesizer, 1, wx.EXPAND, 5 )

		finishedsizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		finishedsizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.panel_finished = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		cSizer = wx.BoxSizer( wx.VERTICAL )

		self.c_Panel1 = wx.Panel( self.panel_finished, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button21 = wx.Button( self.c_Panel1, wx.ID_ANY, u"Not Finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		cSizer1.Add( self.m_button21, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.c_Panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		cSizer1.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self.c_Panel1, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		cSizer1.Add( self.m_button22, 0, wx.ALL, 5 )


		self.c_Panel1.SetSizer( cSizer1 )
		self.c_Panel1.Layout()
		cSizer1.Fit( self.c_Panel1 )
		cSizer.Add( self.c_Panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.c_Panel2 = wx.Panel( self.panel_finished, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button23 = wx.Button( self.c_Panel2, wx.ID_ANY, u"Not Finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button23.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		cSizer2.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.c_Panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		cSizer2.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self.c_Panel2, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		cSizer2.Add( self.m_button24, 0, wx.ALL, 5 )


		self.c_Panel2.SetSizer( cSizer2 )
		self.c_Panel2.Layout()
		cSizer2.Fit( self.c_Panel2 )
		cSizer.Add( self.c_Panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.c_Panel3 = wx.Panel( self.panel_finished, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button25 = wx.Button( self.c_Panel3, wx.ID_ANY, u"Not Finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button25.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		cSizer3.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.c_Panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		cSizer3.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self.c_Panel3, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		cSizer3.Add( self.m_button26, 0, wx.ALL, 5 )


		self.c_Panel3.SetSizer( cSizer3 )
		self.c_Panel3.Layout()
		cSizer3.Fit( self.c_Panel3 )
		cSizer.Add( self.c_Panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.c_Panel4 = wx.Panel( self.panel_finished, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button27 = wx.Button( self.c_Panel4, wx.ID_ANY, u"Not Finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button27.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		cSizer4.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.c_Panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		cSizer4.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( self.c_Panel4, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button28.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		cSizer4.Add( self.m_button28, 0, wx.ALL, 5 )


		self.c_Panel4.SetSizer( cSizer4 )
		self.c_Panel4.Layout()
		cSizer4.Fit( self.c_Panel4 )
		cSizer.Add( self.c_Panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.c_Panel5 = wx.Panel( self.panel_finished, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button29 = wx.Button( self.c_Panel5, wx.ID_ANY, u"Not Finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button29.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		cSizer5.Add( self.m_button29, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.c_Panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		cSizer5.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_button30 = wx.Button( self.c_Panel5, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button30.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		cSizer5.Add( self.m_button30, 0, wx.ALL, 5 )


		self.c_Panel5.SetSizer( cSizer5 )
		self.c_Panel5.Layout()
		cSizer5.Fit( self.c_Panel5 )
		cSizer.Add( self.c_Panel5, 1, wx.EXPAND |wx.ALL, 5 )


		self.panel_finished.SetSizer( cSizer )
		self.panel_finished.Layout()
		cSizer.Fit( self.panel_finished )
		finishedsizer.Add( self.panel_finished, 1, wx.EXPAND |wx.ALL, 5 )


		nomain.Add( finishedsizer, 1, wx.EXPAND, 5 )


		main.Add( nomain, 1, wx.EXPAND, 5 )

		nomain2 = wx.BoxSizer( wx.HORIZONTAL )

		CalnedarioSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.m_calendar1 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		CalnedarioSizer.Add( self.m_calendar1, 0, wx.ALL, 5 )


		nomain2.Add( CalnedarioSizer, 1, wx.EXPAND, 5 )

		sizerfinal = wx.BoxSizer( wx.HORIZONTAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer27.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer27.Add( self.m_dirPicker1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Elige nombre de fichero", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer27.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_textCtrlSave = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrlSave, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"Done!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_button31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sizerfinal.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer28.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.json*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer28.Add( self.m_filePicker1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Done!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button32, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sizerfinal.Add( bSizer28, 1, wx.EXPAND, 5 )


		nomain2.Add( sizerfinal, 1, wx.EXPAND, 5 )


		main.Add( nomain2, 1, wx.EXPAND, 5 )


		self.SetSizer( main )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.TD_St1 )
		self.m_button2.Bind( wx.EVT_BUTTON, self.TD_X1 )
		self.m_button3.Bind( wx.EVT_BUTTON, self.TD_St2 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.TD_X2 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.TD_St3 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.TD_X3 )
		self.m_button7.Bind( wx.EVT_BUTTON, self.TD_St4 )
		self.m_button8.Bind( wx.EVT_BUTTON, self.TD_X4 )
		self.m_button9.Bind( wx.EVT_BUTTON, self.TD_St5 )
		self.m_button10.Bind( wx.EVT_BUTTON, self.TD_X5 )
		self.m_button11.Bind( wx.EVT_BUTTON, self.IC_Do1 )
		self.m_button12.Bind( wx.EVT_BUTTON, self.IC_X1 )
		self.m_button13.Bind( wx.EVT_BUTTON, self.IC_Do2 )
		self.m_button14.Bind( wx.EVT_BUTTON, self.IC_X2 )
		self.m_button15.Bind( wx.EVT_BUTTON, self.IC_Do3 )
		self.m_button16.Bind( wx.EVT_BUTTON, self.IC_X3 )
		self.m_button17.Bind( wx.EVT_BUTTON, self.IC_Do4 )
		self.m_button18.Bind( wx.EVT_BUTTON, self.IC_X4 )
		self.m_button19.Bind( wx.EVT_BUTTON, self.IC_Do5 )
		self.m_button20.Bind( wx.EVT_BUTTON, self.IC_X5 )
		self.m_button21.Bind( wx.EVT_BUTTON, self.Fi_NF1 )
		self.m_button22.Bind( wx.EVT_BUTTON, self.Fi_X1 )
		self.m_button23.Bind( wx.EVT_BUTTON, self.Fi_NF2 )
		self.m_button24.Bind( wx.EVT_BUTTON, self.Fi_X2 )
		self.m_button25.Bind( wx.EVT_BUTTON, self.Fi_NF3 )
		self.m_button26.Bind( wx.EVT_BUTTON, self.Fi_X3 )
		self.m_button27.Bind( wx.EVT_BUTTON, self.Fi_NF4 )
		self.m_button28.Bind( wx.EVT_BUTTON, self.Fi_X4 )
		self.m_button29.Bind( wx.EVT_BUTTON, self.Fi_NF5 )
		self.m_button30.Bind( wx.EVT_BUTTON, self.Fi_X5 )
		self.m_button31.Bind( wx.EVT_BUTTON, self.save_1 )
		self.m_button32.Bind( wx.EVT_BUTTON, self.open_1 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def TD_St1( self, event ):
		event.Skip()

	def TD_X1( self, event ):
		event.Skip()

	def TD_St2( self, event ):
		event.Skip()

	def TD_X2( self, event ):
		event.Skip()

	def TD_St3( self, event ):
		event.Skip()

	def TD_X3( self, event ):
		event.Skip()

	def TD_St4( self, event ):
		event.Skip()

	def TD_X4( self, event ):
		event.Skip()

	def TD_St5( self, event ):
		event.Skip()

	def TD_X5( self, event ):
		event.Skip()

	def IC_Do1( self, event ):
		event.Skip()

	def IC_X1( self, event ):
		event.Skip()

	def IC_Do2( self, event ):
		event.Skip()

	def IC_X2( self, event ):
		event.Skip()

	def IC_Do3( self, event ):
		event.Skip()

	def IC_X3( self, event ):
		event.Skip()

	def IC_Do4( self, event ):
		event.Skip()

	def IC_X4( self, event ):
		event.Skip()

	def IC_Do5( self, event ):
		event.Skip()

	def IC_X5( self, event ):
		event.Skip()

	def Fi_NF1( self, event ):
		event.Skip()

	def Fi_X1( self, event ):
		event.Skip()

	def Fi_NF2( self, event ):
		event.Skip()

	def Fi_X2( self, event ):
		event.Skip()

	def Fi_NF3( self, event ):
		event.Skip()

	def Fi_X3( self, event ):
		event.Skip()

	def Fi_NF4( self, event ):
		event.Skip()

	def Fi_X4( self, event ):
		event.Skip()

	def Fi_NF5( self, event ):
		event.Skip()

	def Fi_X5( self, event ):
		event.Skip()

	def save_1( self, event ):
		event.Skip()

	def open_1( self, event ):
		event.Skip()


