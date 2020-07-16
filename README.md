# energy-efficiency-prediction
Regression for heating and cooling load of buildings


Data:
https://archive.ics.uci.edu/ml/datasets/Energy+efficiency

#### Survey paper on Multi-target regression
http://oa.upm.es/40804/1/INVE_MEM_2015_204213.pdf

Configure docker locally

`docker-machine rm default`

`docker-machine create -d virtualbox --virtualbox-cpu-count=1 --virtualbox-
memory=4094 default
`

### Requesting predictions
To request a prediction, create a post request to the server of the format:
`curl CONTAIN_IP:80/ -d "{\"X1\": \"10\", \"X2\": \"10\", \"X3\": \"10\", \"X4\": \"10\",\"X5\": \"10\", \"X6\": \"10\", \"X7\": \"10\", \"X8\": \"10\"}" -H 'Content-Type:application/json'`
note: The quotes are escaped for use on windows cmd.
### Training methods
All models were trained in Ipython notebooks using sklearn.
An 80/20 train/test split was performed and 5-fold cross validation was performed on the training set.

### Model results

| Model | Train Error (MSE) | Test Error (MSE) |
|-------|-------------------|------------------|
|Single Target SGDRegressor |9.95 |7.57                  |
|Multitarget Ridge|9.79|7.59|
|Multitarget Ridge dropped colums|10.34|7.85|
|RegressionTree|1.48|1.75|
|ExtraTree| 1.63|1.82|
|RandomForest|1.31|1.51|