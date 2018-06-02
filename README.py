# Cricket-Score-Predictor-Albert-version
Predicts the score of team in 20 overs 

print("welcome to Cricket Score Predictor !")
print("CSP albert")
from datetime import datetime
timenow=datetime.now()
print (timenow)
team=input("which is the team batting first?")
print ("Let us see how how many runs "+team+" score in 20 overs")
runs=input("how many runs have been scored?")
runs_float=float(runs)
overs=input("how many overs have been bowled?")
overs_float=float(overs)
wickets=input("how many wickets have fallen?")
wickets_float=float(wickets)
runrate=runs_float/overs_float
runs_e=runrate*24
wicket_loss=5*wickets_float
runsp=runs_e-wicket_loss
runs_predicted=str(int(runsp))
if runsp>239.0 or runsp<120.0:
    print("the predicted score is "+runs_predicted+" but prediction not suitable at this stage of the innings!sorry for the inconvenience :(")
else:
    print(runs_predicted+" is the predicted score for "+team+" in 20 overs!")
