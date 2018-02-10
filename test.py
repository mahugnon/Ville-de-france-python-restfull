import pandas as pd
import os
import numpy as np
from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'It works!'})

@app.route('/ville/<string:numdep>/<string:code_postal>',methods=['GET'])
def ville(numdep,code_postal):
    df=pd.read_csv('C:/Users/Honore/Desktop/Todo/Test/villes_france.csv',header=None)
    df.columns=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple', 'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone', 'ville_code_postal', 'ville_commune','ville_code_commune','ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010', 'ville_population_1999', 'ville_population_2012', 'ville_densite_2010', 'ville_surface', 'ville_longitude_deg', 'ville_latitude_deg', 'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms', 'ville_latitude_dms', 'ville_zmin', 'ville_zmax']
    df.ville_code_postal=[i.lstrip('0') for i in df.ville_code_postal]
    val=df.loc[(df.ville_departement==numdep) & (df.ville_code_postal==code_postal)]
    return val.to_json()
    
    
if __name__=='__main__':
    app.run(debug=True,port=8080)