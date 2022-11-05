# -*- coding: utf-8 -*-
import tkinter as tk
import requests
from jma_weather import get_weathers
from google_calendar import get_schedules
import sys

class Application(tk.Frame):
    """ Tkinter Application
    """
    def __init__(self, master=None, root_size=[400,200], widgets=[]):
        """__init__ method.
        Args:
            master (class tkinter.Tk): root.
            root_size (list): List of root size.
            widgets (list): List of widgets.
        """
        super().__init__(master)
        self.root_size = root_size
        self.widgets = widgets
        master.title(" ")
        master.geometry(f"400x200+0+0")
        self.pack()

    def update(self):
        """update method.
        Update at regular intervals.
        """
        weather, date, time, temp, precip = get_weathers()
        temps = [temp["min"], temp["max"]]
        precips = [precip["min"], precip["max"]]
        schedules = get_schedules()
        self.widgets = [weather, date, time, schedules, temps, precips]
        self.create_widgets(self.widgets)
        self.after(600000, self.update)

    def create_widgets(self, widgets):
        """ create_widgets method.
        Create widgets.
        Args:
            widgets(list) : List of widgets(weather, date, time, schedules, temps, precips).
        """
        text_color = "black"

        weather, date, time, schedules, temps, precips = widgets

        # Create Frame(left, right)
        frame_left = tk.Frame(self.master, bg = "#dde7f1")
        frame_right = tk.Frame(self.master, bg = "#dde7f1")

        fr_left_relw, fr_left_relh = 0.5, 1.0
        fr_right_relw, fr_right_relh = 0.5, 1.0

        frame_left.place(
            relx = 0.0, rely = 0.0, 
            relwidth = fr_left_relw, relheight = fr_left_relh, 
        )
        frame_right.place(
            relx = 0.5,rely = 0.0, 
            relwidth = fr_right_relw, relheight = fr_right_relh, 
        )

        # Create Frame(fr_left_up, fr_left_bm)
        fr_left_up_relw, fr_left_up_relh = 1.0, 0.5
        fr_left_bm_relw, fr_left_bm_relh = 1.0, 0.5
        frame_left_up = tk.Frame(frame_left, bg = "#dde7f1")
        frame_left_up.place(
            relx = 0.0, rely = 0.0,
            relwidth = fr_left_up_relw, relheight = fr_left_up_relh, 
        )
        frame_left_bm = tk.Frame(frame_left, bg = "#dde7f1")
        frame_left_bm.place(
            relx = 0, rely = 0.5, 
            relwidth = fr_left_bm_relw, relheight = fr_left_bm_relh, 
        )

        # Create Frame(fr_left_up_2, fr_left_bm_2) 
        fr_left_up_2_relw, fr_left_up_2_relh = 0.95, 0.9
        fr_left_bm_2_relw, fr_left_bm_2_relh = 0.95, 0.9
        fr_left_up_2_relx, fr_left_up_2_rely = 0.025, 0.05
        fr_left_bm_2_relx, fr_left_bm_2_rely = 0.025, 0.05
        frame_left_up_2 = tk.Frame(frame_left_up, bg="#e6ecf3")
        frame_left_up_2.place(
            relx=fr_left_up_2_relx, rely=fr_left_up_2_rely,
            relwidth=fr_left_up_2_relw, relheight = fr_left_up_2_relh
        )
        frame_left_bm_2 = tk.Frame(frame_left_bm, bg="#e6ecf3")
        frame_left_bm_2.place(
            relx=fr_left_bm_2_relx, rely=fr_left_bm_2_rely,
            relwidth=fr_left_bm_2_relw, relheight = fr_left_bm_2_relh
        )
        
        # temp
        lb_temp_title_relh = 0.2
        lb_temp_label_relh = 0.8
        lb_temp_title_size = int((self.root_size[1]*fr_left_up_relh*fr_left_up_2_relh*lb_temp_title_relh)/1.5)
        ## temp title
        lb_temp = tk.Label(
            frame_left_up_2, text="temp",
            fg="black", bg="#e6ecf3", font=("Helvetica", lb_temp_title_size) 
        )
        lb_temp.place(
            relx=0.0, rely=0.0,
            relwidth = 1.0, relheight = lb_temp_title_relh
        )
        
        lb_temp_text_size = int((self.root_size[1]*fr_left_up_relh*fr_left_up_2_relh*lb_temp_label_relh)/3)
        ## temp_max
        lb_temp_max = tk.Label(
            frame_left_up_2, text=f"{temps[1]}°", 
            fg="black", bg="#e6ecf3", font=("Helvetica", lb_temp_text_size) 
        )
        lb_temp_max.place(
            relx=0.0, rely=lb_temp_title_relh,
            relwidth = 0.5, relheight = lb_temp_label_relh
        )
        ## temp_min
        lb_temp_min = tk.Label(
            frame_left_up_2, text=f"{temps[0]}°", 
            fg="black", bg="#e6ecf3", font=("Helvetica", lb_temp_text_size) 
        )
        lb_temp_min.place(
            relx=0.5, rely=lb_temp_title_relh,
            relwidth = 0.5, relheight = lb_temp_label_relh
        )
        

        # precip
        lb_precip_title_relh = 0.2
        lb_precip_label_relh = 0.8
        lb_precip_title_size = lb_temp_title_size
        lb_precip = tk.Label(
            frame_left_bm_2, text="precip",
            fg="black", bg="#e6ecf3", font=("Helvetica", lb_precip_title_size)
        )
        lb_precip.place(
            relx=0.0, rely=0.0,
            relwidth = 1.0, relheight = lb_precip_title_relh
        )
        ## precip_max
        lb_precip_text_size = lb_temp_text_size
        lb_precip_max = tk.Label(
            frame_left_bm_2, text=f"{precips[1]}%",
            fg="black", bg="#e6ecf3", font=("Helvetica", lb_precip_text_size)
        )
        lb_precip_max.place(
            relx=0.0, rely=lb_precip_title_relh,
            relwidth = 0.5, relheight = lb_precip_label_relh
        )
        ## precip_min
        lb_precip_min = tk.Label(
            frame_left_bm_2, text=f"{precips[0]}%",
            fg="black", bg="#e6ecf3", font=("Helvetica", lb_precip_text_size) 
        )
        lb_precip_min.place(
            relx=0.5, rely=lb_precip_title_relh,
            relwidth = 0.5, relheight = lb_precip_label_relh
        )

        # frame_right_2
        fr_right_2_relw, fr_right_2_relh = 0.95, 0.95
        fr_right_2_relx, fr_right_2_rely = 0.025, 0.05/2
        
        frame_right_2 = tk.Frame(frame_right, bg = "#e6ecf3")
        frame_right_2.place(
            relx = fr_right_2_relx, rely = fr_right_2_rely,
            relwidth = fr_right_2_relw, relheight = fr_right_2_relh, 
        )

        ## schedules
        for i in range(len(schedules)):
            lb3 = tk.Label(
                frame_right_2, text=f"{schedules[i]}", 
                anchor="w", fg="black", bg="#e6ecf3", font=("Helvetica", )
            )
            lb3.place(
                relx=0.0, rely=1.0/len(schedules)*i,
                relwidth= 1.0, relheight=1.0/len(schedules),
            )

def main():
    weather, date, time, temp, precip = get_weathers()
    temps = [temp["min"], temp["max"]]
    precips = [precip["min"], precip["max"]]
    schedules = get_schedules()
    root = tk.Tk()
    app = Application(
        master=root, 
        widgets=[weather, date, time, schedules, temps, precips])
    app.update()
    app.mainloop()

if __name__=="__main__":
    main()