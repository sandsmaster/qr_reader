from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        # Create a vertical BoxLayout as the root widget
        root_layout = GridLayout(cols=2)

        # Add three labels
        label1 = Label(text='Label 1')
        label2 = Label(text='Label 2')
        label3 = Label(text='Label 3')

        # Add three buttons
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')
        button3 = Button(text='Button 3')

        # Add widgets to the layout
        root_layout.add_widget(label1)
        root_layout.add_widget(button1)
        root_layout.add_widget(label2)
        root_layout.add_widget(button2)
        root_layout.add_widget(label3)
        root_layout.add_widget(button3)

        return root_layout

if __name__ == '__main__':
    MyApp().run()

#img_path = r'C:\Users\Vager\Desktop\Slavi_QR\qr_codes\cool_qr.png'
#qr_text = r'https://www.youtube.com/watch?v=jIQ6UV2onyI'