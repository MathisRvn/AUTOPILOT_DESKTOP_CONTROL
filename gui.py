import tkinter
import tkinter.ttk
import _thread
import time



win = tkinter.Tk()
win.geometry('500x200')
win.title("Desktop interface - Pterodactaile")


port_pick_label = tkinter.Label(text="Select board port:")
port_pick_combobox = None
port_refresh_list = None
port_connect_button = None


command_string_var = tkinter.StringVar()
command_string_var.set("Command:")
command_label = tkinter.Label(win, textvariable=command_string_var)

output_string_raw_var = tkinter.StringVar()
output_string_raw_var.set("Output raw:")
output_raw_label = tkinter.Label(win, textvariable=output_string_raw_var)

output_axis_string_var = tkinter.StringVar()
output_axis_string_var.set("Output axis:")
output_axis_label = tkinter.Label(win, textvariable=output_axis_string_var)

attitude_string_var = tkinter.StringVar()
attitude_string_var.set("Attitude:")
attitude_label = tkinter.Label(win, textvariable=attitude_string_var)

# TODO : add memory fetch and display
# TODO : add clean memroy
# TODO : display data / export data csv




def start (ard):

    port_pick_combobox = tkinter.ttk.Combobox(values=ard.getListPort())
    port_refresh_list = tkinter.Button(text="R", command=lambda: port_pick_combobox.config(values=ard.getListPort()))
    port_connect_button = tkinter.Button(text="Connect", command=lambda: ard.setPort(port_pick_combobox.get()))


    port_pick_label.grid(row=0, column=0)
    port_pick_combobox.grid(row=0, column=1)

    port_refresh_list.grid(row=0, column=2)
    port_connect_button.grid(row=0, column=3)

    command_label.grid(row=2, column=0)
    output_raw_label.grid(row=3, column=0)
    output_axis_label.grid(row=4, column=0)
    attitude_label.grid(row=5, column=0)


    win.mainloop()


def update(ard):
    # TODO : print data in a prettier way
    command_string_var.set("Command: " + str(ard.command))
    output_string_raw_var.set("Output raw: " + str(ard.output_raw))
    output_axis_string_var.set("Output axis: " + str(ard.output_axis))
    attitude_string_var.set("Attitude: " + str(ard.attitude))
