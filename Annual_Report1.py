from datetime import datetime
from fpdf import FPDF
import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
import matplotlib.pyplot as plt

class PDF(FPDF):
    def header(self):
        # Line break
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


    def chapter_title(self, label):
        # Arial 12
        self.set_font('Times', 'B', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, '%s' % (label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def print_chapter_title(self, label):
        self.add_page()
        self.chapter_title(label)

    def print_text(self, name, name1):
        self.df = pd.read_excel(name, sheet_name=name1)

        # creating a pdf in called test.pdf in the current directory

        self.set_font('Times', '', 12)
        for i in range(0, len(self.df)):
            col_a = str(self.df['col1'].loc[i])
            self.multi_cell(0, 5, col_a)
            self.ln()
        self.ln(2)

    def print_text_note(self, name, name1):
        self.df1 = pd.read_excel(name, sheet_name=name1)

        # creating a pdf in called test.pdf in the current directory

        self.set_font('Times', 'I', 10)
        for i in range(0, len(self.df1)):
            col_a = str(self.df1['col1'].loc[i])
            self.multi_cell(0, 3, col_a)
            self.ln()
        self.ln(2)

date=datetime.today().strftime('%d %B %Y')

pdf = PDF()
pdf.add_page()
pdf.set_line_width(2)
pdf.set_draw_color(255, 0, 0)
pdf.line(90, 42, 90, 128)
pdf.set_font('Times', '', 36)
pdf.set_text_color(0,0,80)
pdf.cell(205,65,'United', align='C')
pdf.ln(2.5)
pdf.set_font('Times', '', 36)
pdf.cell(206,90,'Money', align='C')
pdf.ln(8.5)
pdf.set_font('Times', '', 36)
pdf.cell(206,105,'Market', align='C')
pdf.ln(9)
pdf.set_font('Times', '', 36)
pdf.cell(197,120,'Fund', align='C')
pdf.ln(12)
pdf.set_font('Times', 'B', 14)
pdf.cell(203,140,'Annual Report', align='C')
pdf.ln(8)
pdf.set_font('Times', 'B', 14)
pdf.cell(197,140,date,align='C')
pdf.ln(10)
pdf.image("logo.PNG", x=100, y=250,w=80)
pdf.add_page()
pdf.set_text_color(0,0,0)
pdf.print_chapter_title("(A) MANAGER'S REPORT")
pdf.ln(5)
pdf.print_text('text/Manager Report_text.xlsx', 'Key Data of the Fund')
df_1 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Breakdown of unit holdings')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 3
pdf.set_font('Times', 'B', 12)
pdf.cell(page_width, 0.0, 'As at 31 January 2021', align='C')
pdf.ln(2)

th = pdf.font_size

pdf.ln(2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_1)):

    col_a = str(df_1['col1'].loc[i])
    col_b = str(df_1['col2'].loc[i])
    col_c = str(df_1['col3'].loc[i])
    if col_a.strip() == 'Total':
            pdf.set_font('Times', 'B', 12)
    pdf.cell(col_width, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.2*th, '%s' % (col_b), 1, 0, 'C')
    pdf.cell(col_width, 1.2*th, '%s' % (col_c), 1, 0, 'R')
    pdf.ln(1.2*th)

pdf.ln(10)
pdf.ln(2)
pdf.print_text('text/Manager Report_text.xlsx', 'Performance Data of the Fund_1')
df_2 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Portfolio composition')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 4
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size
pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_2)):

    col_a = str(df_2['col1'].loc[i])
    col_b = str(df_2['col2'].loc[i])
    col_c = str(df_2['col3'].loc[i])
    col_d = str(df_2['col4'].loc[i])
    if col_a.strip() == 'Total':
        pdf.set_font('Times', 'B', 12)
    #pdf.get_x()
    #pdf.get_y()
    top = pdf.y
    offset = pdf.x + 70
    pdf.multi_cell(70, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    #pdf.set_xy(pdf.get_x() + col_width, pdf.get_y())
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.2*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.2*th, '%s' % (col_c), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 80
    pdf.multi_cell(40, 1.2*th, '%s' % (col_d), 1, 0, 'C')

    #pdf.ln(th)

pdf.ln(10)
pdf.ln(2)
pdf.print_text('text/Manager Report_text.xlsx', 'Performance Data of the Fund_2')
df_3 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Performance details')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 4
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size
pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_3)):

    col_a = str(df_3['col1'].loc[i])
    col_b = str(df_3['col2'].loc[i])
    col_c = str(df_3['col3'].loc[i])
    col_d = str(df_3['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 75
    pdf.multi_cell(75, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(38, 1.2*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 38
    pdf.multi_cell(38, 1.2*th, '%s' % (col_c), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 76
    pdf.multi_cell(38, 1.2*th, '%s' % (col_d), 1, 0, 'C')

    #pdf.ln(th)
pdf.ln(2)
pdf.print_text_note('text/Manager Report_text.xlsx', 'Performance Data of the Fund_3')
pdf.ln(5)
df_4 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Average total return')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 2
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_4)):

    col_a = str(df_4['col1'].loc[i])
    col_b = str(df_4['col2'].loc[i])
    pdf.cell(col_width, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.2*th, '%s' % (col_b), 1, 0, 'C')

    pdf.ln(1.2*th)
pdf.ln(10)
df_5 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Annual total return')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 2
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_5)):

    col_a = str(df_5['col1'].loc[i])
    col_b = str(df_5['col2'].loc[i])
    pdf.cell(col_width, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.2*th, '%s' % (col_b), 1, 0, 'C')

    pdf.ln(1.2*th)
pdf.ln(10)
pdf.print_text('text/Manager Report_text.xlsx', 'Annual total return_Note')
pdf.image("graph1.PNG", w=190)
pdf.ln(2)
pdf.print_text_note('text/Manager Report_text.xlsx', 'Graph source')
pdf.ln(2)
df2=pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Performance review_graph')

c = [2.0, 4.0, 6.0, 8.0, 10.0]
m = [x - 0.5 for x in c]

xticks(c, df2['Types'])

plt.plot(m, df2['The Fund'], color="blue", label="The Fund")
plt.plot(c, df2['Benchmark'], color="red", label="Benchmark")

legend()
axis([0, 12, 0, 25])
savefig('linegraph.PNG')
pdf.image("linegraph.PNG", w=190)
pdf.ln(2)
pdf.print_text_note('text/Manager Report_text.xlsx', 'Graph source')
pdf.ln(5)
df_6 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Performance review')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 6
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size

pdf.ln(2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_6)):

    col_a = str(df_6['col1'].loc[i])
    col_b = str(df_6['col2'].loc[i])
    col_c = str(df_6['col3'].loc[i])
    col_d = str(df_6['col4'].loc[i])
    col_e = str(df_6['col5'].loc[i])
    col_f = str(df_6['col6'].loc[i])
    top = pdf.y
    offset = pdf.x + 28
    pdf.multi_cell(28, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(28, 1.2*th, '%s' % (col_b), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+28
    pdf.multi_cell(28, 1.2*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+56
    pdf.multi_cell(28, 1.2*th, '%s' % (col_d), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+84
    pdf.multi_cell(28, 1.2*th, '%s' % (col_e), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+112
    pdf.multi_cell(50, 1.2*th, '%s' % (col_f), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.print_text_note("text/Manager Report_text.xlsx",'Performance review_asterisk')
pdf.print_text("text/Manager Report_text.xlsx", 'Performance review')
df_7 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Asset allocation')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 4
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size

pdf.ln(2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_7)):

    col_a = str(df_7['col1'].loc[i])
    col_b = str(df_7['col2'].loc[i])
    col_c = str(df_7['col3'].loc[i])
    col_d = str(df_7['col4'].loc[i])
    pdf.cell(col_width, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.2*th, '%s' % (col_b), 1, 0, 'C')
    pdf.cell(col_width, 1.2*th, '%s' % (col_c), 1, 0, 'C')
    pdf.cell(col_width, 1.2*th, '%s' % (col_d), 1, 0, 'C')

    pdf.ln(1.2*th)
pdf.ln(5)
pdf.print_text("text/Manager Report_text.xlsx", 'Asset allocation')
df_8 = pd.read_excel('table/Manager Report_table.xlsx', sheet_name='Income distribution')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', '', 12)
col_width = page_width / 4
pdf.set_font('Times', 'B', 12)
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_8)):

    col_a = str(df_8['col1'].loc[i])
    col_b = str(df_8['col2'].loc[i])
    col_c = str(df_8['col3'].loc[i])
    col_d = str(df_8['col4'].loc[i])
    pdf.cell(col_width, 1.2*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.2*th, '%s' % (col_b), 1, 0, 'C')
    pdf.cell(col_width, 1.2*th, '%s' % (col_c), 1, 0, 'C')
    pdf.cell(col_width, 1.2*th, '%s' % (col_d), 1, 0, 'C')

    pdf.ln(1.2*th)
pdf.ln(5)
pdf.print_text("text/Manager Report_text.xlsx", 'Income distribution')
pdf.set_font('Times', '', 12)
pdf.cell(0,0,date,align='L')
pdf.ln(2)
pdf.print_chapter_title("(B) TRUSTEE'S REPORT")
pdf.ln(5)
pdf.print_text('text/Trustee Report_text.xlsx', 'Trustee Report')
pdf.ln(10)
df_9 = pd.read_excel('table/Trustee Report_table.xlsx', sheet_name='Trustee Report_table')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 2
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_9)):

    col_a = str(df_9['col1'].loc[i])
    col_b = str(df_9['col2'].loc[i])
    pdf.cell(col_width, th, '%s' % (col_a), 0, 0, 'L')
    pdf.cell(col_width, th, '%s' % (col_b), 0, 0, 'L')

    pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Trustee Report_text.xlsx', 'Trustee Report_1')
pdf.cell(0,0,date,align='L')
pdf.ln(5)
pdf.print_chapter_title("(C) STATEMENT BY MANAGER")
pdf.ln(5)
pdf.print_text('text/Statement by Manager_text.xlsx', 'Statement by Manager')
pdf.ln(20)
pdf.print_text('text/Statement by Manager_text.xlsx', 'Statement by Manager_1')
df_10 = pd.read_excel('table/Statement by Manager_table.xlsx', sheet_name='Statement by Manager')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 2
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_10)):

    col_a = str(df_10['col1'].loc[i])
    col_b = str(df_10['col2'].loc[i])
    pdf.cell(col_width, th, '%s' % (col_a), 0, 0, 'L')
    pdf.cell(col_width, th, '%s' % (col_b), 0, 0, 'L')

    pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Statement by Manager_text.xlsx', 'Statement by Manager_2')
pdf.cell(0,0,date,align='L')
pdf.ln(5)
pdf.print_chapter_title("(D) Independent auditors' report to the unitholders of")
pdf.print_text('text/Independent auditors report_text.xlsx', 'Independent auditors report')
pdf.ln(15)
df_11 = pd.read_excel('table/Independent auditors report_table.xlsx', sheet_name='Independent auditors report')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 2
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_11)):

    col_a = str(df_11['col1'].loc[i])
    col_b = str(df_11['col2'].loc[i])
    pdf.cell(col_width, th, '%s' % (col_a), 0, 0, 'L')
    pdf.cell(col_width, th, '%s' % (col_b), 0, 0, 'L')

    pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Independent auditors report_text.xlsx', 'Independent auditors report_1')
pdf.cell(0,0,date,align='L')
pdf.ln(5)
pdf.print_chapter_title("(E) FINANCIAL STATEMENTS")
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Position')
pdf.ln(5)
df_12 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Financial Position')

#creating a pdf in called test.pdf in the current directory
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_12)):

    col_a = str(df_12['col1'].loc[i])
    col_b = str(df_12['col2'].loc[i])
    col_c = str(df_12['col3'].loc[i])
    col_d = str(df_12['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 90
    pdf.multi_cell(90, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(20, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+20
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+60
    pdf.multi_cell(40, 1.5*th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(20)
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Position_1')
pdf.add_page()
pdf.print_text('text/Financial Statement_text.xlsx', 'Comprehensive Income')
df_13 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Comprehensive Income')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_13)):

    col_a = str(df_13['col1'].loc[i])
    col_b = str(df_13['col2'].loc[i])
    col_c = str(df_13['col3'].loc[i])
    col_d = str(df_13['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 90
    pdf.multi_cell(90, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(20, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+20
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+60
    pdf.multi_cell(40, 1.5*th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(20)
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Position_1')
pdf.add_page()
pdf.print_text('text/Financial Statement_text.xlsx', 'Changes in Net Asset Value')
df_14 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Changes in Net Asset Value')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 5
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_14)):

    col_a = str(df_14['col1'].loc[i])
    col_b = str(df_14['col2'].loc[i])
    col_c = str(df_14['col3'].loc[i])
    col_d = str(df_14['col4'].loc[i])
    col_e = str(df_14['col5'].loc[i])
    top = pdf.y
    offset = pdf.x + 65
    pdf.multi_cell(65, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(20, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+20
    pdf.multi_cell(35, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+55
    pdf.multi_cell(35, 1.5*th, '%s' % (col_d), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 90
    pdf.multi_cell(35, 1.5 * th, '%s' % (col_e), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(20)
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Position_1')
pdf.add_page()
pdf.print_text('text/Financial Statement_text.xlsx', 'Cash Flows')
df_15 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Cash Flows')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_15)):

    col_a = str(df_15['col1'].loc[i])
    col_b = str(df_15['col2'].loc[i])
    col_c = str(df_15['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(20)
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Position_1')
pdf.add_page()
pdf.print_text('text/Financial Statement_text.xlsx', 'Notes Financial Statement')
df_16 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Deposit Licensed Financial_1')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_16)):

    col_a = str(df_16['col1'].loc[i])
    col_b = str(df_16['col2'].loc[i])
    col_c = str(df_16['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(2)
pdf.print_text('text/Financial Statement_text.xlsx', 'Deposit Licensed Financial_1')
df_17 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Deposit Licensed Financial_2')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_17)):

    col_a = str(df_17['col1'].loc[i])
    col_b = str(df_17['col2'].loc[i])
    col_c = str(df_17['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(10)
pdf.print_text('text/Financial Statement_text.xlsx', 'Amount Due Manager')
df_18 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Amount Due Manager')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_18)):

    col_a = str(df_18['col1'].loc[i])
    col_b = str(df_18['col2'].loc[i])
    col_c = str(df_18['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(2)
pdf.print_text('text/Financial Statement_text.xlsx', 'Amount Due Manager_1')
pdf.add_page()
pdf.print_text('text/Financial Statement_text.xlsx', 'Amount Due to Trustee')
df_19 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Amount Due to Trustee')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_19)):

    col_a = str(df_19['col1'].loc[i])
    col_b = str(df_19['col2'].loc[i])
    col_c = str(df_19['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(2)
pdf.print_text('text/Financial Statement_text.xlsx', 'Amount Due to Trustee_1')
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Unitholders Equity')
df_20 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Unitholders Equity')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_20)):

    col_a = str(df_20['col1'].loc[i])
    col_b = str(df_20['col2'].loc[i])
    col_c = str(df_20['col3'].loc[i])
    col_d = str(df_20['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 90
    pdf.multi_cell(90, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(20, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+20
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+60
    pdf.multi_cell(40, 1.5*th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Unitholders Equity_a')
df_21 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Unitholders Equity_a')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.ln(4.2)
pdf.set_font('Times', '', 12)
for i in range(0, len(df_21)):

    col_a = str(df_21['col1'].loc[i])
    col_b = str(df_21['col2'].loc[i])
    col_c = str(df_21['col3'].loc[i])
    col_d = str(df_21['col4'].loc[i])
    col_e = str(df_21['col5'].loc[i])
    top = pdf.y
    offset = pdf.x + 58
    pdf.multi_cell(58, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(33, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+33
    pdf.multi_cell(33, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset+66
    pdf.multi_cell(33, 1.5*th, '%s' % (col_d), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 99
    pdf.multi_cell(33, 1.5 * th, '%s' % (col_e), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Unitholders Equity_a_1')
df_22 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Unitholders Equity_b')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_22)):

    col_a = str(df_22['col1'].loc[i])
    col_b = str(df_22['col2'].loc[i])
    col_c = str(df_22['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Manager Fee')
df_23 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Income Tax Expense')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_23)):

    col_a = str(df_23['col1'].loc[i])
    col_b = str(df_23['col2'].loc[i])
    col_c = str(df_23['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(20)
pdf.print_text('text/Financial Statement_text.xlsx', 'Distributions')
df_24 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Distributions')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_24)):

    col_a = str(df_24['col1'].loc[i])
    col_b = str(df_24['col2'].loc[i])
    col_c = str(df_24['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 110
    pdf.multi_cell(110, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(40, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+40
    pdf.multi_cell(40, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Distributions_1')
df_25 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Distributions_1')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_25)):

    col_a = str(df_25['col1'].loc[i])
    col_b = str(df_25['col2'].loc[i])
    col_c = str(df_25['col3'].loc[i])
    col_d = str(df_25['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 50
    pdf.multi_cell(50, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(50, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+50
    pdf.multi_cell(45, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 95
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.add_page()
df_26 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Distributions_2')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_26)):

    col_a = str(df_26['col1'].loc[i])
    col_b = str(df_26['col2'].loc[i])
    col_c = str(df_26['col3'].loc[i])
    col_d = str(df_26['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 50
    pdf.multi_cell(50, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(50, 1.5*th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset+50
    pdf.multi_cell(45, 1.5*th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 95
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Management Expense Ratio')
df_27 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Management Expense Ratio')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_27)):

    col_a = str(df_27['col1'].loc[i])
    col_b = str(df_27['col2'].loc[i])
    col_c = str(df_27['col3'].loc[i])
    pdf.cell(col_width, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.5*th, '%s' % (col_b), 1, 0, 'R')
    pdf.cell(col_width, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    pdf.ln(1.5*th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Management Expense Ratio_1')
df_28 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Portfolio Turnover Ratio')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_28)):

    col_a = str(df_28['col1'].loc[i])
    col_b = str(df_28['col2'].loc[i])
    col_c = str(df_28['col3'].loc[i])
    pdf.cell(col_width, 1.5*th, '%s' % (col_a), 1, 0, 'L')
    pdf.cell(col_width, 1.5*th, '%s' % (col_b), 1, 0, 'R')
    pdf.cell(col_width, 1.5*th, '%s' % (col_c), 1, 0, 'R')

    pdf.ln(1.5*th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Portfolio Turnover Ratio')
pdf.add_page()
pdf.print_text('text/Financial Statement_text.xlsx', 'Other Financial Institutions')
df_29 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Other Financial Institutions')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_29)):

    col_a = str(df_29['col1'].loc[i])
    col_b = str(df_29['col2'].loc[i])
    col_c = str(df_29['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 80
    pdf.multi_cell(80, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(55, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 55
    pdf.multi_cell(55, 1.5 * th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Instruments')
pdf.add_page()
df_30 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Financial Instruments')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_30)):

    col_a = str(df_30['col1'].loc[i])
    col_b = str(df_30['col2'].loc[i])
    col_c = str(df_30['col3'].loc[i])
    col_d = str(df_30['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 55
    pdf.multi_cell(55, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 45
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 90
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(10)
df_31 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Financial Instruments_1')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_31)):

    col_a = str(df_31['col1'].loc[i])
    col_b = str(df_31['col2'].loc[i])
    col_c = str(df_31['col3'].loc[i])
    col_d = str(df_31['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 55
    pdf.multi_cell(55, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 45
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 90
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(5)
pdf.print_text('text/Financial Statement_text.xlsx', 'Financial Instruments_1')
df_32 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Credit Risk')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_32)):

    col_a = str(df_32['col1'].loc[i])
    col_b = str(df_32['col2'].loc[i])
    col_c = str(df_32['col3'].loc[i])
    col_d = str(df_32['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 55
    pdf.multi_cell(55, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 45
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 90
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(2)
pdf.print_text('text/Financial Statement_text.xlsx', 'Credit Risk')
df_33 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Credit Risk_1')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 4
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_33)):

    col_a = str(df_33['col1'].loc[i])
    col_b = str(df_33['col2'].loc[i])
    col_c = str(df_33['col3'].loc[i])
    col_d = str(df_33['col4'].loc[i])
    top = pdf.y
    offset = pdf.x + 55
    pdf.multi_cell(55, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 45
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_c), 1, 0, 'R')
    pdf.y = top
    pdf.x = offset + 90
    pdf.multi_cell(45, 1.5 * th, '%s' % (col_d), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(2)
pdf.print_text('text/Financial Statement_text.xlsx', 'Credit Risk_1')
pdf.add_page()
df_34 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Credit Risk_2')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_34)):

    col_a = str(df_34['col1'].loc[i])
    col_b = str(df_34['col2'].loc[i])
    col_c = str(df_34['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 70
    pdf.multi_cell(70, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(60, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 60
    pdf.multi_cell(60, 1.5 * th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(10)
df_35 = pd.read_excel('table/Financial Statement_table.xlsx', sheet_name='Credit Risk_3')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 3
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_35)):

    col_a = str(df_35['col1'].loc[i])
    col_b = str(df_35['col2'].loc[i])
    col_c = str(df_35['col3'].loc[i])
    top = pdf.y
    offset = pdf.x + 70
    pdf.multi_cell(70, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(60, 1.5 * th, '%s' % (col_b), 1, 0, 'C')
    pdf.y = top
    pdf.x = offset + 60
    pdf.multi_cell(60, 1.5 * th, '%s' % (col_c), 1, 0, 'R')

    #pdf.ln(1.5*th)
pdf.ln(10)
pdf.print_text('text/Financial Statement_text.xlsx', 'Capital Management')
pdf.print_chapter_title("(F) CORPORATE INFORMATION")
df_36 = pd.read_excel('table/Corporate Information_table.xlsx', sheet_name='Corporate Information')
pdf.set_line_width(0.1)
pdf.set_draw_color(0, 0, 0)
page_width = pdf.w - 2 * pdf.l_margin

col_width = page_width / 2
pdf.ln(1)

th = pdf.font_size

pdf.set_font('Times', '', 12)
for i in range(0, len(df_36)):

    col_a = str(df_36['col1'].loc[i])
    col_b = str(df_36['col2'].loc[i])
    top = pdf.y
    offset = pdf.x + 70
    pdf.multi_cell(70, 1.5 * th, '%s' % (col_a), 1, 0, 'L')
    pdf.y = top
    pdf.x = offset
    pdf.multi_cell(120, 1.5 * th, '%s' % (col_b), 1, 0, 'C')

    #pdf.ln(1.5*th)
pdf.ln(5)
pdf.output('report1.pdf', 'F')

