import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image, ImageTk

#functions
def upload_file():
    global img
    global image_last
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    image_last = Image.open(filename)
    image_show_button =tk.Button(my_ui,image=img) # using Button
    image_show_button.grid(row=3,column=1)

def get_color():
    colors = askcolor(title="Tkinter Color Chooser")
    global watermark_color
    watermark_color = colors[1]


def add_watermark():
    # watermark options
    width, height = image_last.size
    draw = ImageDraw.Draw(image_last)
    watermark = watermark_entry.get()
    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(watermark, font)
    margin = 10
    x_cord = width - textwidth - margin
    y_cord = height - textheight - margin
    if watermark_color == None:
        draw.text((x_cord, y_cord), watermark, font=font, fill='black')
    else:
        draw.text((x_cord, y_cord), watermark, font=font,fill=watermark_color)
    image_last.show()
    image_last.save('ImageWithWatemark.jpg')




# User interface
my_ui = tk.Tk()
my_ui.geometry("1080x900")  # Size of the window
my_ui.title('Watermark adder')
my_font1=('times', 18, 'bold')
label1 = tk.Label(my_ui,text='Add Photo',width=30,font=my_font1)
photo_upload_button = tk.Button(my_ui, text='Upload File',
   width=20,command=upload_file)
color_select_button = tk.Button(
    my_ui,
    text='Select your watermarks Color',
    command=get_color)
color_select_button.grid(row=2, column=2)
watermark_entry = tk.Entry()
watermark_entry.config(width=25,font=('Arial', 20))
watermark_entry.insert(0, "Write here your watermark")
add_watermark_button = tk.Button(my_ui, text='Add Water Mark',
   width=20,command=add_watermark)
add_watermark_button.grid(row=3, column=2)
label1.grid(row=1,column=1)
photo_upload_button.grid(row=2,column=1)
watermark_entry.grid(row=1,column=2)


my_ui.mainloop()