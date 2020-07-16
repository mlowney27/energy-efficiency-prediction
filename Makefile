DIR := ${CURDIR}

build:
	docker build -t energy-efficiency-prediction:latest -f Dockerfile .

run-dev:
	docker run -d --name mycontainer -p 80:80 energy-efficiency-prediction:latest


build-notebook:
	docker build -t notebook:latest -f training\Dockerfile .
notebook:
	docker run --rm -p 8888:8888 -v //c/Users/Michael/Documents/carbon_relay/energy-efficiency-prediction:/train notebook:latest
