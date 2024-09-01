from flask import Flask, request, jsonify,render_template
from sudoku_solver import solve_sudoku 
from flask_cors import CORS

app = Flask(__name__, static_folder="../login-page/build", static_url_path="/")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/solve', methods=['GET','POST'])
def solve():
    if request.method=='POST':
        sudoku = request.get_json().get('sudoku')

        # Call the Sudoku solver function
        solved_sudoku = solve_sudoku(sudoku)

        response = {'solved_sudoku': solved_sudoku}
        return jsonify(response)
CORS(app)
@app.route('/image', methods=['POST'])
def process_image():
    from imageprocessing import imageprocess
    if 'image' not in request.files:
        return 'No image file found', 400
    if 'image' in request.files:
        image = request.files['image']
        image.save('uploaded_image.jpg')
        
        imageprocess('uploade_image.jpg')
    # imageprocess('')
#         '''
#         OCR code starts here'''
        


    

#     # Return the extracted text as JSON response
    return jsonify({'text': image})

if __name__ == '__main__':
    app.run(debug=True)