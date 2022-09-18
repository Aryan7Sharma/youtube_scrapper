from flask import Flask, request, render_template, jsonify
import scrapping
import logging
from flask_cors import CORS,cross_origin

app = Flask(__name__)
logging.basicConfig(filename="loggers/app.txt", level=logging.INFO, format='%(filename)s: %(levelname)s: %(message)s: %(asctime)s')
logs = logging.getLogger()
@app.route('/', methods=['GET']) # route to display home page
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/scrapped_data',methods=["GET","POST"])
@cross_origin()
def search():
    """
    :return: scrapped_data web page
    """
    if request.method == 'POST':
        try:
            name = request.form['content']
            number_of_videos = int(request.form['number'])
            interaction_time = int(request.form['interaction_time'])
            alldata_in_2darray = scrapping.fetching_all_data(name, number_of_videos, interaction_time)
            videos_data = []
            for i in range(len(alldata_in_2darray[0])):
                logs.info("we are in for loop %s", i)
                dict = {"Title": alldata_in_2darray[0][i], "Videos_url": alldata_in_2darray[1][i], "Thumbnail": alldata_in_2darray[2][i], "Views": alldata_in_2darray[3][i], "Likes": alldata_in_2darray[4][i], "Total_Comments": alldata_in_2darray[5][i], "Commenter": alldata_in_2darray[6][str(i)], "Comments": alldata_in_2darray[7][str(i)]}
                logs.info("dict created %s", dict)
                logs.info("my dict %s", dict)
                videos_data.append(dict)
            logs.info("%s",videos_data)
            return render_template('scrapped_data.html', videos_data=videos_data[0:len(videos_data)])
        except Exception as e:
            logs.exception(e)
            return render_template("index.html")

    else:
        return render_template("index.html")

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)




