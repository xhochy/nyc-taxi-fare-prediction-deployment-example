% : docker/Dockerfile.%
	docker build -t nyc-taxi-$@ -f $< .
