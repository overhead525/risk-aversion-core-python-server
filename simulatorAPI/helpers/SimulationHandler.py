import json
import os
import uuid
import subprocess

from ..models import SimulationResult, Configuration

core = "C:/Users/ritch/PycharmProjects/SimulationExecutionGateway/SimulationEGAPI/simulatorAPI/executables/"
coreFile = "forex_profit_calc_cpp.exe"
output = "./simulationResult.json"


def executeSimulation(
        principal: float,
        riskDecimal: float,
        rewardDecimal: float,
        winDecimal: float,
        lossDecimal: float,
        breakEvenDecimal: float,
        numOfTrades: int,
        numOfSimulations: int
):
    thisSimID = uuid.uuid4()

    simConfig = Configuration()
    simConfig.simID = thisSimID
    simConfig.principal = principal
    simConfig.riskDecimal = riskDecimal
    simConfig.rewardDecimal = rewardDecimal
    simConfig.winDecimal = winDecimal
    simConfig.lossDecimal = lossDecimal
    simConfig.breakEvenDecimal = breakEvenDecimal
    simConfig.numOfTrades = numOfSimulations
    simConfig.numOfSimulations = numOfSimulations

    subprocess.run([
        f'{core}{coreFile}',
        str(principal),
        str(riskDecimal),
        str(rewardDecimal),
        str(winDecimal),
        str(lossDecimal),
        str(breakEvenDecimal),
        str(numOfTrades),
        str(numOfSimulations)
    ])

    if os.path.isfile(output):
        print('FILE HAS BEEN MADE')
    else:
        raise ValueError("FILE DOES NOT EXIST")

    with open(output) as f:
        simulationOutput = json.load(f)

    simResult = SimulationResult()
    simResult.simID = thisSimID
    simResult.maxPortfolio = round(simulationOutput["maxPortfolioAmount"], 2)
    simResult.minPortfolio = round(simulationOutput["minPortfolioAmount"], 2)

    simConfig.save()
    simResult.save()
    return simResult


if __name__ == '__main__':
    try:
        result = executeSimulation(100000, 0.01, 0.03, 0.55, 0.45, 0.25, 50, 1000)
        print(result.minPortfolio)
    except TypeError:
        pass
