#!/usr/bin/env bash

./analyzeResults.py LVTestCaseUsingAusgridData_Mon_bus_ LVTestCaseUsingAusgridData_EXP_METERS.CSV ../results/ ../resultsAnalysis/
./analyzeResults.py LVTestCaseUsingAusgridDataWithPV_Mon_bus_ LVTestCaseUsingAusgridDataWithPV_EXP_METERS.CSV ../results/ ../resultsAnalysis/
./analyzeResults.py LVTestCaseUsingAusgridDataWithPVandEV_Mon_bus_ LVTestCaseUsingAusgridDataWithPVandEV_EXP_METERS.CSV ../results/ ../resultsAnalysis/
./analyzeResults.py LVTestCaseUsingAusgridDataWithPVandEVBalanced_Mon_bus_ LVTestCaseUsingAusgridDataWithPVandEVBalanced_EXP_METERS.CSV ../results/ ../resultsAnalysis/
./analyzeResults.py LVTestCaseUsingAusgridDataWithPVandEV2Phase_Mon_bus_ LVTestCaseUsingAusgridDataWithPVandEV2Phase_EXP_METERS.CSV ../results/ ../resultsAnalysis/


./plotFeederPower.py ../results/LVTestCaseUsingAusgridData_Mon_feederpower.csv ../resultsAnalysis/LVTestCaseUsingAusgridData_feedepower.pdf

./plotFeederPower.py ../results/LVTestCaseUsingAusgridDataWithPV_Mon_feederpower.csv ../resultsAnalysis/LVTestCaseUsingAusgridDataWithPV_feedepower.pdf

./plotFeederPower.py ../results/LVTestCaseUsingAusgridDataWithPVandEV_Mon_feederpower.csv ../resultsAnalysis/LVTestCaseUsingAusgridDataWithPVandEV_feedepower.pdf

./plotFeederPower.py ../results/LVTestCaseUsingAusgridDataWithPVandEVBalanced_Mon_feederpower.csv ../resultsAnalysis/LVTestCaseUsingAusgridDataWithPVandEVBalanced_feedepower.pdf

./plotFeederPower.py ../results/LVTestCaseUsingAusgridDataWithPVandEV2Phase_Mon_feederpower.csv ../resultsAnalysis/LVTestCaseUsingAusgridDataWithPVandEV2Phase_feedepower.pdf


