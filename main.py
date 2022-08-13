import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("SMARTHOME")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="ADD",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_addPreferences = customtkinter.CTkButton(master=self.frame_left,
                                                text="addPreference",
                                                command=self.button_add_preference_event)
        self.button_addPreferences.grid(row=2, column=0, pady=10, padx=20)

        self.button_addSensor = customtkinter.CTkButton(master=self.frame_left,
                                                text="addSensor",
                                                command=self.button_add_sensor_event)
        self.button_addSensor.grid(row=3, column=0, pady=10, padx=20)

        self.button_addActuator = customtkinter.CTkButton(master=self.frame_left,
                                                text="addActuator",
                                                command=self.button_add_actuator_event)
        self.button_addActuator.grid(row=4, column=0, pady=10, padx=20)
        
        self.button_modify_actuator = customtkinter.CTkButton(master=self.frame_left,
                                                text="ModifyActuator",
                                                command=self.button_modify_actuator_event)
        self.button_modify_actuator.grid(row=5, column=0, pady=10, padx=20)

        self.button_remove = customtkinter.CTkButton(master=self.frame_left,
                                                text="RemoveInstances",
                                                border_color="red", fg_color=("#E52B50"),
                                                command=self.button_remove_event)
        self.button_remove.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3,4,5,6), weight=1)
        self.frame_right.rowconfigure(6, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=2, pady=10, padx=20, sticky="nsew")
        
        self.frame_info_sensor = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info_sensor.grid(row=2, column=0, columnspan=2, rowspan=2, pady=10, padx=20, sticky="nsew")
        
        self.frame_info_actuator = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info_actuator.grid(row=4, column=0, columnspan=2, rowspan=2, pady=10, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(1, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        self.label_InfoValues = customtkinter.CTkLabel(master=self.frame_info,
                                              text="INFO",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_InfoValues.grid(row=0, column=0, pady=1, padx=1)
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text= 
                                                    "location: " + str(location)+" \n" +
                                                    "day: " + str(day)+" \n" +
                                                    "time: " + str(time)+" \n" +
                                                    "skyinfo: " + str(skyinfo)+" \n",
                                                    # "tempOutisde: " + str(tempOutisde)+" \n" +
                                                    # "wind: " + str(wind)+" \n" +
                                                    # "db: " + str(db)+" \n" +
                                                    # "temperatureInside: " + str(temperatureInside)+" \n" +
                                                    # "brightness: " + str(brightness)+" \n" ,
                                                   corner_radius=6,  # <- custom corner radius
                                                   text_font=("Consolas", -12),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=1, sticky="w", padx=5, pady=5)
 

        # self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        # self.progressbar.grid(row=2, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_info_sensor ============
        self.frame_info_sensor.rowconfigure(1, weight=1)
        self.frame_info_sensor.columnconfigure(0, weight=1)
        self.label_InfoValuesSensor = customtkinter.CTkLabel(master=self.frame_info_sensor,
                                              text="SENSORS VALUES",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_InfoValuesSensor.grid(row=2, column=0, pady=1, padx=1)
        sensors = getAllSensor()
        text1 = ""
        for k,v in sensors.items():
            text1 += str(k) + ": " + str(v[0])+ " "+  str(v[1]) +"\n"
        self.label_info_sensor_1 = customtkinter.CTkLabel(master=self.frame_info_sensor,
                                                    text= text1,
                                                    corner_radius=6,  # <- custom corner radius
                                                    text_font=("Consolas", -12),  # <- custom tuple-color
                                                    justify=tkinter.LEFT)
        self.label_info_sensor_1.grid(column=0, row=3, sticky="w", padx=5, pady=5)
        
        

        
        # ============ frame_info_actuator ============

        self.frame_info_actuator.rowconfigure(1, weight=1)
        self.frame_info_actuator.columnconfigure(0, weight=1)
        self.label_InfoValuesActuator = customtkinter.CTkLabel(master=self.frame_info_actuator,
                                              text="ACTUATORS VALUES",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_InfoValuesActuator.grid(row=4, column=0, pady=1, padx=1)
        actuators = getAllActuator()
        text1 = ""
        for k,v in actuators.items():
            text1 += str(k) + ": " + str(v[0])+ " "+  str(v[1]) +"\n"
        self.label_info_actuator_1 = customtkinter.CTkLabel(master=self.frame_info_actuator,
                                                    text= text1,
                                                    corner_radius=6,  # <- custom corner radius
                                                    text_font=("Consolas", -12),
                                                    justify=tkinter.LEFT)
        self.label_info_actuator_1.grid(column=0, row=5, sticky="w", padx=5, pady=5)

        # ============ frame_right ============

        self.label_prefmenu = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Select mode:")
        self.label_prefmenu.grid(row=0, column=2, columnspan=1, pady=5, padx=10, sticky="")
        
        
        setOfValues = getAllPreferences()
        values1 = []
        for e in setOfValues:
            values1.append(e)
        self.prefmenu = customtkinter.CTkComboBox(master=self.frame_right,
                                                        values=values1,
                                                        command=self.change_prefernceMode)  
        self.prefmenu.grid(row=1, column=2, pady=10, padx=20, sticky="we")

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=0, text="Pref1")
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=1, text="Pref2")
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=2, text="Pref3")
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        # self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         command=self.progressbar.set)
        # self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
        # self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.switch_2 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
        # self.switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
        #                                             values=["Value 1", "Value 2"])
        # self.combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=0, padx=20, sticky="w")

        # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_2.grid(row=6, column=1, pady=0, padx=20, sticky="w")

        # self.entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="CTkEntry")
        # self.entry.grid(row=8, column=0, columnspan=2, pady=0, padx=20, sticky="we")

        self.button_refresh = customtkinter.CTkButton(master=self.frame_right,
                                                text="Refresh",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.refresh)
        self.button_refresh.grid(row=5, column=2, columnspan=1, pady=20, padx=20, sticky="se")

        # set default values
        self.optionmenu_1.set("Dark")
        # self.button_addActuator.configure(state="disabled", text="Disabled CTkButton")
        # self.combobox_1.set("CTkCombobox")
        # self.radio_button_1.select()
        self.prefmenu.set("NoPreference")
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.switch_2.select()
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()
        
    def button_modify_actuator_event(self):
        window_sensor = Modify_Actuator()
        window_sensor.mainloop()
        
    def button_remove_event(self):
        window_sensor = Remove()
        window_sensor.mainloop()        

    def button_event(self):
        print("Button pressed")
        
    def button_add_sensor_event(self):
        window_sensor = Add_Sensor()
        window_sensor.mainloop()


        
    def button_add_actuator_event(self):
        window_actuator = Add_Actuator()
        window_actuator.mainloop()

        
    def button_add_preference_event(self):
        print("wowoow")
        window_preference = Add_Preference()
        window_preference.mainloop()
        
    def change_prefernceMode(self, preference):
        print(preference)
        if preference != "NoPreference":
            setPreference(preference)
            self.refresh()
        

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def on_closing(self, event=0):
        self.destroy()
        
        
    def refresh(self):
        
        actuators = getAllActuator()
        text1 = ""
        for k,v in actuators.items():
            text1 += str(k) + ": " + str(v[0])+ " "+  str(v[1]) +"\n"     
        self.label_info_actuator_1.configure(text=text1)

        sensors = getAllSensor()
        print(sensors)
        text1 = ""
        for k,v in sensors.items():
            text1 += str(k) + ": " + str(v[0])+ " "+  str(v[1]) +"\n"
        self.label_info_sensor_1.configure(text=text1)
        
        setOfValues = getAllPreferences()
        values1 = []
        for e in setOfValues:
            values1.append(e)
        lastvalue = self.prefmenu.get()
        
        self.prefmenu.configure(values=values1) 
        # customtkinter.CTkComboBox(master=self.frame_right,
        #                                                 values=values1,
        #                                                 command=self.change_prefernceMode)  
        # self.prefmenu.grid(row=1, column=2, pady=10, padx=20, sticky="we")
        # self.prefmenu.set(lastvalue)


class Add_Sensor(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x260")
        self.title("ADD SENSOR")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)

        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)

        # self.settings_image = self.load_image("/test_images/settings.png", 20)
        # self.bell_image = self.load_image("/test_images/bell.png", 20)
        # self.add_folder_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_list_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_user_image = self.load_image("/test_images/add-user.png", 20)
        # self.chat_image = self.load_image("/test_images/chat.png", 20)
        # self.home_image = self.load_image("/test_images/home.png", 20)
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_1,
                                              text="Insert sensor name: ",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0,columnspan=2,padx=20, pady=(20, 10), sticky="ew")
        
        self.entry = customtkinter.CTkEntry(master=self.frame_1,
                                            width=120,
                                            placeholder_text="sensor name...")
        self.entry.grid(row=2, column=0, columnspan=2,padx=20, pady=10, sticky="ew")

        
        setOfValues = getAllType()
        values1 = []
        for e in setOfValues:
            values1.append(e)
            
        self.typemenu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=values1)  
        self.typemenu.grid(row=3, column=0, columnspan = 2, padx=20, pady=10, sticky="s")
        
        self.typemenu.set(values1[0])
        
        self.radio_var = tkinter.IntVar(value=0)
        
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=0, text="Inside")
        self.radio_button_1.grid(row=4, column=0, pady=10, padx=20, sticky="sw")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=1, text="Outside")
        self.radio_button_2.grid(row=4, column=1, pady=10, padx=20, sticky="se")
        
        self.radio_button_1.select()
    

        self.button_5 = customtkinter.CTkButton(master=self,  text="Add Sensor", width=130, height=60, border_width=2,
                                                corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function)
        self.button_5.grid(row=0, column=1, padx=20, pady=20)


    def button_function(self):
        typeSensor = ""
        nameSensor = ""
        print("button pressed")
        nameSensor = self.entry.get()
        print(self.entry.get())
        typeSensor = self.typemenu.get()
        location = ""
        print(self.typemenu.get())
        if (self.radio_var):
            location= "outside"
        else: location = "inside"
        
        if(setSensorType(nameSensor, typeSensor, location)):
            self.destroy()
            app.refresh()
        else: 
            while(True):
                dialog = customtkinter.CTkInputDialog(master=None, text="Sensor name already used, choose another one:", title="Error Name")
                

                name = dialog.get_input()
                if(name!="" and setSensorType(name, typeSensor,location)):
                    self.destroy()
                    app.refresh()
                    break
                    
            

class Add_Actuator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x260")
        self.title("ADD ACTUATOR")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)

        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)

        # self.settings_image = self.load_image("/test_images/settings.png", 20)
        # self.bell_image = self.load_image("/test_images/bell.png", 20)
        # self.add_folder_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_list_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_user_image = self.load_image("/test_images/add-user.png", 20)
        # self.chat_image = self.load_image("/test_images/chat.png", 20)
        # self.home_image = self.load_image("/test_images/home.png", 20)
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_1,
                                              text="Insert actuator name: ",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0,columnspan=2,padx=20, pady=(20, 10), sticky="ew")
        
        self.entry = customtkinter.CTkEntry(master=self.frame_1,
                                            width=120,
                                            placeholder_text="actuator name...")
        self.entry.grid(row=2, column=0, columnspan=2,padx=20, pady=10, sticky="ew")

        
        setOfValues = getAllType()
        values1 = []
        for e in setOfValues:
            values1.append(e)
            
        self.typemenu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=values1)  
        self.typemenu.grid(row=3, column=0, columnspan = 2, padx=20, pady=10, sticky="s")
        
        self.typemenu.set(values1[0])
        
        self.radio_var = tkinter.IntVar(value=0)
        
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=0, text="Inside")
        self.radio_button_1.grid(row=4, column=0, pady=10, padx=20, sticky="sw")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=1, text="Outside")
        self.radio_button_2.grid(row=4, column=1, pady=10, padx=20, sticky="se")
        
        self.radio_button_1.select()

        self.button_5 = customtkinter.CTkButton(master=self,  text="Add Actuator", width=130, height=60, border_width=2,
                                                corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function)
        self.button_5.grid(row=0, column=1, padx=20, pady=20)

    # def load_image(self, path, image_size):
    #     """ load rectangular image with path relative to PATH """
    #     return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def button_function(self):
        typeActuator = ""
        nameActuator = ""
        print("button pressed")
        nameActuator = self.entry.get()
        print(self.entry.get())
        typeActuator = self.typemenu.get()
        print(self.typemenu.get())
        if (self.radio_var):
            location= "outside"
        else: location = "inside"
        
        if(setActuatorType(nameActuator, typeActuator, location)):
            self.destroy()
            app.refresh()
        else: 
            while(True):
                dialog = customtkinter.CTkInputDialog(master=None, text="Actuator name already used, choose another one:", title="Error Name")
                name = dialog.get_input()
                if(name!="" and setActuatorType(name, typeActuator, location)):
                    self.destroy()
                    app.refresh()
                    break
                    

class Modify_Actuator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x520")
        self.title("MODIFY ACTUATOR")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)

        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)

        # self.settings_image = self.load_image("/test_images/settings.png", 20)
        # self.bell_image = self.load_image("/test_images/bell.png", 20)
        # self.add_folder_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_list_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_user_image = self.load_image("/test_images/add-user.png", 20)
        # self.chat_image = self.load_image("/test_images/chat.png", 20)
        # self.home_image = self.load_image("/test_images/home.png", 20)
        
        self.label_2 = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Preference Value: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=1, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        

        self.slider = customtkinter.CTkSlider(master=self.frame_1,
                                                from_=0,
                                                to=100,
                                                command=self.slider_event)
        self.slider.grid(row=2, column=0, columnspan=4, pady=2, padx=10, sticky="we")
        self.slider.set(10)
        
        self.label_slider = customtkinter.CTkLabel(master=self.frame_1,
                                             text=str(self.slider.get()),
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_slider.grid(row=2, column=1,pady=2, padx=0, sticky="e")
 
        self.label_Type = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose Type: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_Type.grid(row=3, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        

        setOfValues = getAllType()
        values1 = []
        for e in setOfValues:
            values1.append(e)
            
        self.property = ""
        self.actuatorChoosen = set()
        self.typemenu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=values1)  
        self.typemenu.grid(row=4, column=0, padx=20, pady=2, sticky="ew")
        
        self.typemenu.set(values1[0])
        self.button_property = customtkinter.CTkButton(master=self.frame_1,  text="Confirm Type", width=30, height=30, border_width=1,
                                                corner_radius=6, compound="bottom", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function_property)
        self.button_property.grid(row=4, column=1, padx=20, pady=2,sticky="ew")
        
        self.label_Actuator = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose Actuators: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_Actuator.grid(row=5, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        

        
        self.actuatorList = ["None"]
        self.actuatormenu = customtkinter.CTkComboBox(master=self.frame_1,values=self.actuatorList)  
        self.actuatormenu.grid(row=6, column=0,padx=20, pady=2, sticky="ew")
                

        self.button_5 = customtkinter.CTkButton(master=self,  text="Confirm Actuator Value", width=130, height=60, border_width=2,
                                                corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function)
        self.button_5.grid(row=0, column=1, padx=20, pady=10)
        

    # def load_image(self, path, image_size):
    #     """ load rectangular image with path relative to PATH """
    #     return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
    
    def slider_event(self, value):
        self.label_slider = customtkinter.CTkLabel(master=self.frame_1,
                                             text=str(int(self.slider.get())),
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_slider.grid(row=2, column=1,pady=2, padx=0, sticky="e")
        
              

    def button_function_property(self):
        self.property = self.typemenu.get()
        self.button_property.configure(state="disabled", text="Property Locked")
        self.button_property.grid(row=4, column=1, padx=20, pady=2)
        tempDict = getAllActuatorByType(self.property)
        tempList = []
        for val in tempDict:
            tempList.append(val)
        
        print(tempList)
        self.actuatormenu = customtkinter.CTkComboBox(master=self.frame_1, values=tempList)  
        self.actuatormenu.grid(row=6, column=0,padx=20, pady=2, sticky="ew")

    def button_function(self):
        setActuatorValue(str(self.actuatormenu.get()), str(int(self.slider.get())))
        self.destroy()
        app.refresh()

        

            
           
                     
           
                

class Add_Preference(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("650x560")
        self.title("ADD PREFERENCE")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)

        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)

        # self.settings_image = self.load_image("/test_images/settings.png", 20)
        # self.bell_image = self.load_image("/test_images/bell.png", 20)
        # self.add_folder_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_list_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_user_image = self.load_image("/test_images/add-user.png", 20)
        # self.chat_image = self.load_image("/test_images/chat.png", 20)
        # self.home_image = self.load_image("/test_images/home.png", 20)
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_1,
                                              text="Insert preference name: ",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        
        self.entry = customtkinter.CTkEntry(master=self.frame_1,
                                            width=120,
                                            placeholder_text="preference name...")
        self.entry.grid(row=2, column=0, columnspan=2,padx=20, pady=2, sticky="ew")

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Preference Value: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=3, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        

        self.slider = customtkinter.CTkSlider(master=self.frame_1,
                                                from_=0,
                                                to=100,
                                                command=self.slider_event)
        self.slider.grid(row=4, column=0, columnspan=4, pady=2, padx=10, sticky="we")
        self.slider.set(10)
        
        self.label_slider = customtkinter.CTkLabel(master=self.frame_1,
                                             text=str(self.slider.get()),
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_slider.grid(row=4, column=1,pady=2, padx=0, sticky="e")
 
        self.label_Type = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose Type: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_Type.grid(row=5, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        

        setOfValues = getAllType()
        values1 = []
        for e in setOfValues:
            values1.append(e)
            
        self.property = ""
        self.actuatorChoosen = set()
        self.typemenu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=values1)  
        self.typemenu.grid(row=6, column=0, padx=20, pady=2, sticky="ew")
        
        self.typemenu.set(values1[0])
        self.button_property = customtkinter.CTkButton(master=self.frame_1,  text="Confirm Type", width=30, height=30, border_width=1,
                                                corner_radius=6, compound="bottom", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function_property)
        self.button_property.grid(row=6, column=1, padx=20, pady=2,sticky="ew")
        
        self.label_Actuator = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose Actuators: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_Actuator.grid(row=7, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        

        
        self.actuatorList = ["None"]
        self.actuatormenu = customtkinter.CTkComboBox(master=self.frame_1,values=self.actuatorList)  
        self.actuatormenu.grid(row=8, column=0,padx=20, pady=2, sticky="ew")
        
        self.button_addActuator = customtkinter.CTkButton(master=self.frame_1,  text="Add Actuator", width=30, height=30, border_width=1,
                                                corner_radius=6, compound="bottom", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function_addActuator)
        self.button_addActuator.grid(row=8, column=1, padx=20, pady=2, sticky="ew")
        
               
        text1=""
        for val in self.actuatorChoosen:
            text1 += str(val) + "\n"
        self.label_info_actuatorChoosen = customtkinter.CTkLabel(master=self.frame_1,
                                                    text= text1,
                                                    corner_radius=6,  # <- custom corner radius
                                                    text_font=("Consolas", -14),  # <- custom tuple-color
                                                    justify=tkinter.LEFT)
        self.label_info_actuatorChoosen.grid( row=10, column=0, columnspan = 2, sticky="s", padx=5, pady=2)
        

        self.button_5 = customtkinter.CTkButton(master=self,  text="Confirm Preference", width=130, height=60, border_width=2,
                                                corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function)
        self.button_5.grid(row=0, column=1, padx=20, pady=10)
        

    # def load_image(self, path, image_size):
    #     """ load rectangular image with path relative to PATH """
    #     return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
    
    def slider_event(self, value):
        self.label_slider = customtkinter.CTkLabel(master=self.frame_1,
                                             text=str(int(self.slider.get())),
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_slider.grid(row=4, column=1,pady=2, padx=0, sticky="e")
        
        
        
    def button_function_addActuator(self):
        self.actuatorChoosen.add(self.actuatormenu.get())
        text1=""
        for val in self.actuatorChoosen:
            text1 += str(val) + "\n"
            
        self.label_ActuatorChoosen = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Actuators Choosen: ",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_ActuatorChoosen.grid(row=9, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
         

        self.label_info_actuatorChoosen = customtkinter.CTkLabel(master=self.frame_1,
                                                    text= text1,
                                                    corner_radius=6,  # <- custom corner radius
                                                    text_font=("Consolas", -14),  # <- custom tuple-color
                                                    fg_color=("white", "gray38"),  # <- custom tuple-color
                                                    justify=tkinter.LEFT)
        
        self.label_info_actuatorChoosen.grid(row=10, column=0, columnspan = 2, sticky="s", padx=5, pady=2)
        
        

    def button_function_property(self):
        self.property = self.typemenu.get()
        self.button_property.configure(state="disabled", text="Property Locked")
        self.button_property.grid(row=6, column=1, padx=20, pady=2)
        tempDict = getAllActuatorByType(self.property)
        tempList = []
        for val in tempDict:
            tempList.append(val)
        
        print(tempList)
        self.actuatormenu = customtkinter.CTkComboBox(master=self.frame_1, values=tempList)  
        self.actuatormenu.grid(row=8, column=0,padx=20, pady=2, sticky="ew")

    def button_function(self):

        namePreference = ""
        print("button pressed")
        namePreference = self.entry.get()
        print(self.entry.get())
        print(self.property)
        acutatorsList = []
        for val in self.actuatorChoosen:
            acutatorsList.append(val)
        
        if(saveNewPreference(namePreference, self.property, self.slider.get(), acutatorsList)):
            self.destroy()
            app.refresh()
        else: 
            while(True):
                dialog = customtkinter.CTkInputDialog(master=None, text="Preference name already used, choose another one:", title="Error Name")
                name = dialog.get_input()
                if(name!="" and saveNewPreference(namePreference, self.property,int(self.slider.get()), acutatorsList)):
                    self.destroy()
                    app.refresh()
                    break
        
            

class Remove(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("650x260")
        self.title("Remove Instances")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)

        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)
        self.frame_1.grid_columnconfigure(2, weight=1)

        # self.settings_image = self.load_image("/test_images/settings.png", 20)
        # self.bell_image = self.load_image("/test_images/bell.png", 20)
        # self.add_folder_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_list_image = self.load_image("/test_images/add-folder.png", 20)
        # self.add_user_image = self.load_image("/test_images/add-user.png", 20)
        # self.chat_image = self.load_image("/test_images/chat.png", 20)
        # self.home_image = self.load_image("/test_images/home.png", 20)
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_1,
                                              text="What to remove? ",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0,columnspan=3,padx=20, pady=(10, 2), sticky="ew")
        
        self.radio_var = tkinter.IntVar(value=0)
        
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=0, text="Sensor",
                                                            command=self.radio_sensor_event)
        self.radio_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=1, text="Actuator",
                                                            command=self.radio_actuator_event)
        self.radio_button_2.grid(row=2, column=1, pady=10, padx=20, sticky="ew")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_1,
                                                            variable=self.radio_var,
                                                            value=2, text="Preference",
                                                            command=self.radio_preference_event)
        self.radio_button_3.grid(row=2, column=2, pady=10, padx=20, sticky="ew")

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1,
                                             text="",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=3, column=0,columnspan=3,padx=20, pady=(10, 2), sticky="ew")
        

        # self.menu = customtkinter.CTkComboBox(master=self.frame_1,
        #                                                 values=values1)  
        # self.menu.grid(row=3, column=0, padx=20, pady=2, sticky="ew")
        
        # self.menu.set(values1[0])
        
        

        self.button_5 = customtkinter.CTkButton(master=self,  text="Remove", width=130, height=60, border_width=2,
                                                corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),
                                                hover_color="#C77C78", command=self.button_function)
        self.button_5.grid(row=0, column=1, padx=20, pady=10)
        

    # def load_image(self, path, image_size):
    #     """ load rectangular image with path relative to PATH """
    #     return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
    
    def radio_actuator_event(self):
        
        self.label_2 = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose the actuator to remove",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=3, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        
        actuatorDict = getAllActuator()
        actuatorList = []
        for k,v in actuatorDict.items():
            actuatorList.append(k)
            
        
        self.menu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=actuatorList)  
        self.menu.grid(row=4, column=0, padx=20, pady=2, sticky="ew")

        
    def radio_sensor_event(self):
    
        self.label_2 = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose the sensor to remove",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=3, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        
        sensorDict = getAllSensor()
        sensorList = []
        for k,v in sensorDict.items():
            sensorList.append(k)
            
        
        self.menu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=sensorList)  
        self.menu.grid(row=4, column=0, padx=20, pady=2, sticky="ew")

        
    def radio_preference_event(self):
        
        self.label_2 = customtkinter.CTkLabel(master=self.frame_1,
                                             text="Choose the preference to remove",
                                             text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=3, column=0,columnspan=2,padx=20, pady=(10, 2), sticky="ew")
        
        preferenceDict = getAllPreferences()
        preferenceList = []
        for e in preferenceDict:
            preferenceList.append(e)
            
        preferenceList.remove("nullPreference")
        self.menu = customtkinter.CTkComboBox(master=self.frame_1,
                                                        values=preferenceList)  
        self.menu.grid(row=4, column=0, padx=20, pady=2, sticky="ew")
       
        

    def button_function(self):
        print(self.menu.get())
        if (removeInstance(self.menu.get())):
            self.destroy()
            app.refresh()
                    
        

location,day,time,skyinfo,tempOutisde,wind,db,temperatureInside,brightness = "None","None","None","None","None","None","None","None","None"
actuators = {}
sensors = {}


if __name__ == "__main__":
    from prolog import * 
    from sensor import *

    from pyswip import Prolog
    initialize()
    location,day,time,skyinfo,tempOutisde,wind,db,temperatureInside,brightness=simulateSensorValues()
   
    
    setSensorValue("brightness_outside", str(brightness))
    setSensorValue("temperature", str(temperatureInside))
    setSensorValue("temperature_outside", str(tempOutisde))
    
    actuators = getAllActuator()

    sensors = getAllSensor()
    print(sensors)
    

    app = App()
    app.mainloop()

    