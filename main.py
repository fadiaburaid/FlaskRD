import pyautogui
from flask import Flask, render_template, Response, request
from screen import VideoScreen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
          
def gen(screen):
    while True:
        frame = screen.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoScreen()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/action_page', methods=['POST'])
def action_page():
    xcoor=request.form.get('xcoor')
    ycoor=request.form.get('ycoor')
    xcoor=int(xcoor)*2
    ycoor=int(ycoor)*2
    print(xcoor)
    print(ycoor)
    pyautogui.click(xcoor,ycoor)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80', debug=True)
