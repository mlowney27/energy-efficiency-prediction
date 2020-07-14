
build:
	docker build -t energy-efficiency-prediction:latest -f Dockerfile .

run-dev:
	docker run --rm -it -p 5000:5000 -e "FLASK_APP=server.py" energy-efficiency-prediction:latest