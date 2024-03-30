import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from zipfile import ZipFile

class ZipApp(App):
    def build(self):
        self.title = 'File Zipper'

        # Layout
        layout = BoxLayout(orientation='vertical', padding=10)

        # File chooser
        self.file_chooser = FileChooserListView()
        self.file_chooser.filters = [lambda folder, filename: os.path.isfile(os.path.join(folder, filename))]
        layout.add_widget(self.file_chooser)

        # Label to display selected file path
        self.selected_file_label = Label(text="Selected file: None")
        layout.add_widget(self.selected_file_label)

        # Button to zip the file
        zip_button = Button(text='Zip Selected File', size_hint=(1, 0.1))
        zip_button.bind(on_press=self.zip_selected_file)
        layout.add_widget(zip_button)

        return layout

    def zip_selected_file(self, instance):
        selected_file = self.file_chooser.selection[0] if self.file_chooser.selection else None

        if selected_file:
            zip_file_name = os.path.splitext(selected_file)[0] + '.zip'
            with ZipFile(zip_file_name, 'w') as zipf:
                zipf.write(selected_file, os.path.basename(selected_file))
            self.selected_file_label.text = f"File zipped and saved as: {zip_file_name}"
        else:
            self.selected_file_label.text = "Please select a file to zip"

if __name__ == '__main__':
    ZipApp().run()
