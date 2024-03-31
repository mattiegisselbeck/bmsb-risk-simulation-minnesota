# Brown Marmorated Stink Bug Risk Simulation and Analysis in Minnesota

![Docker Cloud Automated build](https://img.shields.io/docker/cloud/build/mattiegisselbeck/bmsb-risk-simulation-minnesota)
![Swagger Validator](https://img.shields.io/swagger/valid/3.0?specUrl=https://bmsb-risk-simulation-minnesota-tr6xl5mv3a-uc.a.run.app/api/v1/doc)
![GitHub last commit](https://img.shields.io/github/last-commit/mattiegisselbeck/bmsb-risk-analysis-minnesota)

## Overview 
Due to the uncertainty of BMSB’s impact in Minnesota, it’s important to track and predict the moving BMSB population. In this project, an end-to-end analysis pipeline is established to help minimize the impact of BMSB in Minnesota by informing decision-makers on where to best deploy mitigation efforts across the State. The objective of this project is to build an automated end-to-end system that identifies municipalities that are likely to face BMSB infestations. In this project, the spread of BMSB populations across Minnesota is modeled using three different spatial interaction models, the simple Huff Model (no distance decay), the Huff Model (distance decay factor of two), and the Gravity Model. Monte Carlo simulation is used in conjunction with these models to develop an understanding of where the population is likely to spread, and therefore where mitigation efforts should be emphasized. Ultimately, these results are made public via an API.

### Data Sources 
EDDMaps. BMSB Observation, Minnesota. <br>
Minnesota Digital Elevation Model - 30 Meter Resolution. U.S. Geological Survey. <br>
IEM. RWIS Weather, Minnesota. <br>
NCLD 2019 Land Cover, Minnesota. <br>
City, Township, and Unorganized Territory in Minnesota. 

### Contributors 
Mattie Gisselbeck
<br>
Luke Zaruba

