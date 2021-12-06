from website import create_app

app= create_app()

#Makes it so that app.run is only executed when file is run and not imported
if __name__== '__main__':
    #debug=true means that any change made to python code causes web server to be rerun
    app.run(debug=True)