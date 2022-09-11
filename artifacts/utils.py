import pickle ,requests
import numpy as np

class prediction():

    def __init__ (self, data):
        self.data = data

    def methode(self):
        with open (r'artifacts/model.pkl' ,'rb') as file:
            self.model = pickle.load(file)

    def result(self):
        self.methode()

        alcohol = float(self.data['alcohol'])
        malic_acid =  float(self.data['malic_acid'])
        ash = float(self.data['ash'])
        alcalinity_of_ash = float(self.data['alcalinity_of_ash'])

        magnesium = float(self.data['magnesium'])

        total_phenols = float(self.data['total_phenols'])
        flavanoids = float(self.data['flavanoids'])
        nonflavanoid_phenols =float(self.data['nonflavanoid_phenols'])
        proanthocyanins = float(self.data['proanthocyanins'])
        color_intensity = float(self.data['color_intensity'])
        hue = float(self.data['hue'])
        diluted_wine = float(self.data['diluted_wine'])
        proline = float(self.data['proline'])

        array =  np.array([[alcohol ,malic_acid ,ash ,alcalinity_of_ash , magnesium ,total_phenols ,
        flavanoids ,nonflavanoid_phenols ,
                 proanthocyanins ,color_intensity ,hue ,proline ,proline ]])

        res = self.model.predict(array)[0]

        return str({'prediction': res })
    
# if __name__ == '__main__':

#     data = {'alcohol' :13.52,'malic_acid':  3.17,'ash' :2.72,'alcalinity_of_ash': 23.5,'magnesium':97,
#             'total_phenols':1.55,'flavanoids': 0.52,'nonflavanoid_phenols':0.50,'proanthocyanins':0.55 ,
#             'color_intensity':4.35 ,'hue' :0.89 , 'diluted_wine':2.06 ,  'proline' :520 }

#     obj = prediction(data)
#     obj.result()
