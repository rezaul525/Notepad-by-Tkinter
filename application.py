import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog,colorchooser,messagebox,font
import os
root = tk.Tk()
root.title('GALXY NOTEPAD')
root.geometry('1200x600')
root.wm_iconbitmap('icon.ico')

# <----------------------------------------------Start Of Main Menu-------------------------------------------->
main_menu = tk.Menu()

#icons
#icon for FIle menu
new_icon = tk.PhotoImage(file='icons_images/add.png')
open_icon = tk.PhotoImage(file='icons_images/folder (1).png')
Save_icon = tk.PhotoImage(file='icons_images/save-file.png')
Save_as_icon = tk.PhotoImage(file='icons_images/save-as.png')
exit_icon = tk.PhotoImage(file='icons_images/exit.png')
#icon for FIle menu

file = tk.Menu(main_menu, tearoff=False)

#End of FIle Menu

#icons For edit
cut_icon = tk.PhotoImage(file='icons_images/paper-cutting.png')
copy_icon = tk.PhotoImage(file='icons_images/copy-two-paper-sheets-interface-symbol.png')
paste_icon = tk.PhotoImage(file='icons_images/clipboard-paste-with-no-format.png')
clear_icon = tk.PhotoImage(file='icons_images/clear.png')
find_icon = tk.PhotoImage(file='icons_images/find.png')
#icon end for edit

edit = tk.Menu(main_menu, tearoff=False)

#end of edit menu

#icon for view
toolbar_icon = tk.PhotoImage(file='icons_images/toolbar.png')
status_icon = tk.PhotoImage(file='icons_images/charging-status.png')

view = tk.Menu(main_menu, tearoff=False)

#end of view
# icons for theme
light_default_icon = tk.PhotoImage(file='icons_images/theme.png')
light_plus_icon = tk.PhotoImage(file='icons_images/theme.png')
dark_icon = tk.PhotoImage(file='icons_images/theme.png')
red_icon = tk.PhotoImage(file='icons_images/theme.png')
monokai_icon = tk.PhotoImage(file='icons_images/theme.png')
night_blue_icon = tk.PhotoImage(file='icons_images/Circle-icon.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme = tk.Menu(main_menu, tearoff=False)
store_theme = tk.StringVar()

color = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
theme_dic = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
    
}



#cascading for file
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Theme',menu=theme)

# <---------------------------------------------End Of Main Menu--------------------------------------------->

# <---------------------------------------Tool bar Start------------------------------------------------------>
# -----Font box-----
main_label = tk.Label(root)
main_label.pack(side=tk.TOP, fill=tk.X)

font_store = tk.StringVar()
main_font = tk.font.families()
box = ttk.Combobox(main_label,textvariable=font_store,width=20,state='readonly')
box.grid(row=0,column=0,padx=5)
box['values'] = main_font
box.current(main_font.index('Arial'))
# ------End of Font box------

# -----size box------
size_store = tk.IntVar()
main_size = ttk.Combobox(main_label,width=15,textvariable=size_store,state='readonly')
main_size.grid(row=0,column=1, padx=5)
main_size['values']= tuple(range(8,40,2))
main_size.current(2)

# -----Button-----
# All icon Sector for button
bold_icon = tk.PhotoImage(file='icons_images/font-style-bold.png')
iatalic_icon = tk.PhotoImage(file='icons_images/italic-letter-style-interface-symbol.png')
underline_icon = tk.PhotoImage(file='icons_images/font-style-underline.png')
align_left_icon = tk.PhotoImage(file='icons_images/align-left.png')
align_center_icon = tk.PhotoImage(file='icons_images/align-center.png')
align_right_icon = tk.PhotoImage(file='icons_images/align.png')
font_color_icon = tk.PhotoImage(file='icons_images/text.png')
# All icon Sector for button

# <---Bold Button Satrt---->
bold_button = ttk.Button(main_label,image=bold_icon)
bold_button.grid(row=0,column=2, padx=5)
# <---Bold Button End----->

# <---italic Button Start---->
italic_button = ttk.Button(main_label,image=iatalic_icon)
italic_button.grid(row=0,column=3, padx=5)
# <---italic Button End---->

# <---Underline Button Start---->
un_button = ttk.Button(main_label,image=underline_icon)
un_button.grid(row=0,column=4,padx=5)
# <---Underline Button End---->

# ----Align Left Button Start----
align_left = ttk.Button(main_label,image=align_left_icon)
align_left.grid(row=0,column=5,padx=6)
# ----Align Left Button End----

# ----Align Cenetr button start---
align_center = ttk.Button(main_label,image=align_center_icon)
align_center.grid(row=0,column=6,padx=5)
# ----Align Center button End---

# ----Align right Button Start----
align_right = ttk.Button(main_label,image=align_right_icon)
align_right.grid(row=0,column=7,padx=5)
# ----Align right Button Start----

# ----Fon color Button start----
color_button = ttk.Button(main_label,image=font_color_icon)
color_button.grid(row=0,column=8,padx=5)
# ----Font color Button End----
# -----Button End---
# <--------------------------------------------------Toolbar End----------------------------------------->


# <----------------------------------------------Main Text Editor Start---------------------------------------------------->
main_text_editor = tk.Text(root)
main_text_editor.config(wrap='word', relief=tk.FLAT)

# Scroll Bar Start
scroll_bar = tk.Scrollbar(root)
main_text_editor.focus_set()

scroll_bar.pack(side=tk.RIGHT, fill=tk. Y)
main_text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=main_text_editor.yview)
main_text_editor.config(yscrollcommand=scroll_bar.set)


#-----------------MainText Editor Funtionality Start-----------
active_font = 'Arial'
active_size = 12
# -------For Font and Size Funtionality-----
def font_change(event=None):
    global active_font
    active_font = font_store.get()
    main_text_editor.configure(font=(active_font,active_size))

box.bind("<<ComboboxSelected>>", font_change)

def size_change(event=None): #no need to pass default arguement in perenthesis ,csn use anything
    global active_size
    active_size = size_store.get()
    main_text_editor.configure(font=(active_font,active_size))

main_size.bind("<<ComboboxSelected>>", size_change)
# -------For Font and Size Funtionality End-----

# <------------------------Start of Button Funtionality---------------------------------->

# -----Bold Button Funtionality Start------
def bold_action():
    text_editor_property = tk.font.Font(font=main_text_editor['font'])
    if text_editor_property.actual()['weight'] == 'normal':
        main_text_editor.configure(font=(active_font,active_size,'bold'))
    if text_editor_property.actual()['weight']=='bold':
        main_text_editor.configure(font=(active_font,active_size,'normal'))
bold_button.configure(command=bold_action)
# -----Bold Button Funtionality End------

# ----Italic button funtionality start----
def italic_action():
    text_editor_property = tk.font.Font(font=main_text_editor['font'])
    if text_editor_property.actual()['slant']=='roman':
        main_text_editor.configure(font=(active_font,active_size,'italic'))
    if text_editor_property.actual()['slant']=='italic':
        main_text_editor.configure(font=(active_font,active_size,'roman'))
italic_button.configure(command=italic_action)
# ----Italic button funtionality End----

# -----Underline Funtionality Start----
def underline_action():
    text_editor_property = tk.font.Font(font=main_text_editor['font'])
    if text_editor_property.actual()['underline']== 0:
        main_text_editor.configure(font=(active_font,active_size, 'underline'))
    if text_editor_property.actual()['underline']==1:
        main_text_editor.configure(font=(active_font,active_size,'normal'))
un_button.configure(command=underline_action)
# -----Underline Funtionality End----

# -----Text Align Funtionality for all Start----
#Left Align Start
def align_left_action():
    left_store = main_text_editor.get(1.0,'end')
    main_text_editor.tag_config('left', justify=tk.LEFT)
    main_text_editor.delete(1.0, tk.END)
    main_text_editor.insert(tk.INSERT, left_store,'left')
align_left.configure(command=align_left_action)
#Left Align End

#Align Center Start
def center_align_action():
    center_store = main_text_editor.get(1.0,'end')
    main_text_editor.tag_config('center', justify=tk.CENTER)
    main_text_editor.delete(1.0, tk.END)
    main_text_editor.insert(tk.INSERT, center_store,'center')
align_center.configure(command=center_align_action)
#End

#Align Right Start
def right_align_action():
    right_store = main_text_editor.get(1.0, 'end')
    main_text_editor.tag_config('right', justify=tk.RIGHT)
    main_text_editor.delete(1.0, tk.END)
    main_text_editor.insert(tk.INSERT,right_store,'right')
align_right.configure(command=right_align_action)
#End
# -----Text Align Funtionality for all End----

# <---------------------------------Font colour functionality start here----------------------------->
def font_color_action():
    color_store = tk.colorchooser.askcolor()
    main_text_editor.configure(fg=color_store[1]) #for hexa colour code use index 1

color_button.configure(command=font_color_action)
# ----Font colour functionality End here----

# <----End of Button Funtionality---->
main_text_editor.configure(font=('Arial', 12))
# <------Text Editor Funtionality End------>
# <-----------------------------------------------Main Text Editor End---------------------------------------------->

# <------------------------------------------------Status bar start------------------------------------------->
status_bar = ttk.Label(root, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

# -----Status bar Funtionality start-----
text_changed = False
def status_action(event=None):
    global text_changed 
    if main_text_editor.edit_modified():
        text_changed = True
        count_word = len(main_text_editor.get(1.0,'end-1c').split())
        count_chrecter = len(main_text_editor.get(1.0, 'end-1c')) #for space count will use replace(' ','') function
        status_bar.config(text=f'Words: {count_word} Charecter: {count_chrecter}')
    main_text_editor.edit_modified(False)
main_text_editor.bind("<<Modified>>", status_action)
# -----Status bar Funtionality End-----
# <---------------------------------------------------Status bar End------------------------------------------------>
# <---------------------------------Main Menu Funtionality Start-------------------------------------->
#Gobal varialbe
url = ''
#function for New file Start
def new_action(event=None):
    global url
    main_text_editor.delete(1.0, tk.END)
#  ----- File Command Start--------
#sub command for file
file.add_command(label='New',image=new_icon, compound=tk.LEFT,accelerator='Ctrl+N',command=new_action)
file.add_separator()
#End function for New File
#funtion for Open File
def open_action(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url, 'r') as fo:
            main_text_editor.delete(1.0, tk.END)
            main_text_editor.insert(1.0, fo.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))

file.add_command(label='Open',image=open_icon, compound=tk.LEFT,accelerator='Ctrl+O', command = open_action)
file.add_separator()
#End of Opnen file function
#Start of Save File Function
def save_action(evnt=None):
    global url
    try:
        if url:
            content = str(main_text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = main_text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return
    
file.add_command(label='Save',image=Save_icon, compound=tk.LEFT,accelerator='Ctrl+S', command=save_action)
file.add_separator()
#end of save functionality
# Save as funtionality Started
def save_as_action(event=None):
    global url
    try:
        content = str(main_text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label='Save As',image=Save_as_icon, compound=tk.LEFT,accelerator='Ctrl+W', command=save_as_action)
file.add_separator()
# Save as funtionality End
# Exit funtionality Started

def exit_action(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning!!!','Do you want to save the file?')
            if mbox is True:
                if url:
                    content = main_text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2 = str(main_text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return

file.add_command(label='Exit', image= exit_icon,compound=tk.LEFT,accelerator='Cltr+Q', command=exit_action)
# Exit funtionality End
#  ----- File Command End--------

#  ----- Edit Command Start--------
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command= lambda: main_text_editor.event_generate('<Control x>'))
edit.add_separator()
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda: main_text_editor.event_generate('Control c'))
edit.add_separator()
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda: main_text_editor.event_generate('Control v'))
edit.add_separator()
edit.add_command(label='Clear All',image=clear_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda: main_text_editor.delete(1.0, tk.END))
edit.add_separator()
#funtionality For Find
# ---Start---
def find_action(event=None):

    def find():
        word = find_entry_box.get()
        main_text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = main_text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                main_text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                main_text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word  = find_entry_box.get()
        replace_txt = replace_input.get()
        content = main_text_editor.get(1.0, tk.END)
        new_content = content.replace(word,replace_txt)
        main_text_editor.delete(1.0, tk.END)
        main_text_editor.insert(1.0, new_content)

    dialog_find = tk.Toplevel()
    dialog_find.geometry('400x250+400+150')
    dialog_find.title('Find')
    dialog_find.resizable(0,0)

    #frame
    main_frame = ttk.LabelFrame(dialog_find, text='Find/Replace')
    main_frame.pack(pady=20)

    #label
    find_label = ttk.Label(main_frame, text='Find: ')
    replace_label = ttk.Label(main_frame, text='Replace: ')

    #entry Box
    find_entry_box = ttk.Entry(main_frame, width=25)
    replace_input = ttk.Entry(main_frame, width=25)

    #button
    find_btn = ttk.Button(main_frame,text='Find',command=find)
    replace_btn = ttk.Button(main_frame,text='Replace',command=replace)

    #grid
    #label
    find_label.grid(row=0,column=0,padx=5,pady=5)
    replace_label.grid(row=1,column=0,padx=5,pady=5)
    #entrybox
    find_entry_box.grid(row=0,column=1,padx=5,pady=5)
    replace_input.grid(row=1,column=1,padx=5,pady=5)
    #btn
    find_btn.grid(row=2,column=0,padx=5,pady=5)
    replace_btn.grid(row=2,column=1,padx=5,pady=5)

    dialog_find.mainloop()
# ---End---
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_action)
#  ----- Edit Command End--------

#  ----- View Command Start--------
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
#funtion for hide toolbar
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        main_label.pack_forget()
        show_toolbar = False
    else:
        main_text_editor.pack_forget()
        status_bar.pack_forget()
        main_label.pack(side=tk.TOP, fill=tk.X)
        main_text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True
#Toolbar Funtion End
view.add_checkbutton(label='Tool bar',onvalue=True,offvalue=0,image=toolbar_icon,variable=show_toolbar,command=hide_toolbar, compound=tk.LEFT,accelerator='Cltr+B')
view.add_separator()
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,image=status_icon,variable=show_statusbar, compound=tk.LEFT,accelerator='Cltr+T',command=hide_statusbar)
#  ----- View Command End--------
#  ----- Theme Command Start-----
def theme_change():
    chossen_theme = store_theme.get()
    color = theme_dic.get(chossen_theme)
    fg_color , bg_color = color[0],color[1]
    main_text_editor.config(background=bg_color,foreground=fg_color)

count = 0
for i in theme_dic:
    theme.add_radiobutton(label= i, image=color[count], variable=store_theme, compound=tk.LEFT, command=theme_change)
    theme.add_separator()
count += 1
#  ----- Theme Command End--------
root.config(menu=main_menu)
# <---------------------------------Main Menu Funtionality End------------------------------------------------->


# <------------For shortcut key----------
#  Binding----------------->
root.bind("<Control-n>",new_action)
root.bind("<Control-o>",open_action)
root.bind("<Control-s>",save_action)
root.bind("<Control-Alt-s>",save_as_action)
root.bind("<Control-q>",exit_action)
root.bind("<Control-f>",find_action)

root.mainloop()
# ------------------------------------------End Of Code----------------------------------