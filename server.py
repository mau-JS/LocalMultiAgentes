from model import *
from agent import *
import numpy as np
import pandas as pd
def agent_portrayal(agent):
        portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "blue",
                 "r": 0.5}
        #Caso en el que sea semáforo
        return portrayal


#results_df = pd.DataFrame(results)
#print(results_df.keys())

grid = mesa.visualization.CanvasGrid(agent_portrayal, 30, 30, 500, 500)
server = mesa.visualization.ModularServer(
    CarModel, [grid], "Car Model", {"N": 5, "width": 30, "height": 30}
)
server.port = 8521 # The default
server.launch()