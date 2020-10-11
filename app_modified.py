from flask import Flask, render_template, request
import pickle

app = Flask(__name__,template_folder = r"C:\**********\*********\ML_AI\Medium") 
                                                                                   
    
clf = pickle.load(open('clf.pkl','rb'))
loaded_vec = pickle.load(open("count_vect.pkl", "rb"))

@app.route('/')

def symptom():
    
   return render_template('symptoms_pred.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['Data']
      result_pred = clf.predict(loaded_vec.transform([result]))
      return render_template("symptoms_result.html",result = result_pred)

if __name__ == '__main__':
   app.run()
