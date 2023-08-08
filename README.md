
# Face-Recognition-Attendance &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/iam7t9/Face-Recognition-Attendance/blob/main/LICENSE)

A simple and easy to use Attendance System


## Tech Stack

**Language:** Python

**Packages:** OpenCV, Tkinter, face_recognition, openpyxl, numpy



## Installation

Supported Python 3.7-3.9

Clone the repo
```bash
git clone https://github.com/iam7t9/Face-Recognition-Attendance.git
cd Face-Recognition-Attendance
```

#### Create Environment

*For Windows*
```powershell
python -m venv env
.\env\Scripts\activate
```
*for Linux*

```bash
python3 -m venv env
source ./env/bin/activate
```

#### Installing Packages

Download dlib compiled wheels suitable for your python version from [Here](https://github.com/sachadee/Dlib)

```bash
pip install <dlib compiled wheels>
pip install -r requirements.txt
```

## Running the Application

- Create folders `faces` and `face_encodings`.
- Add images with ids as name in the faces directory.
- For the first time, generate encoadings for faces. Uncomment the `app.train()` in `main.py` file

```python
if __name__=="__main__":
    # Create the Tkinter window
    window = tk.Tk()
    # Create the CameraApp instance
    app = CameraApp(window)

    # Uncomment following line to generate encodings 
    # app.train()
    # Run the Tkinter event loop    
    window.mainloop()
```


#### Run the application

```bash
python main.py
```

*The attendance record will be added in the database.xlsx file*
## Screenshots

![App Screenshot](https://github.com/iam7t9/Face-Recognition-Attendance/blob/main/ScreenShots/ui.png?raw=true)


## Contributing

Contributions are always welcome!



## Authors

- [@Shantanu Pande](https://www.github.com/iam7t9)
- [@Astha Dhapodkar](https://github.com/AsthaDhapodkar)
