% : docker/Dockerfile.%
	docker buildx build -t nyc-taxi-$@ --load -f $< .

lock:
	conda lock --mamba -p osx-64 -p osx-arm64 -p linux-64 -p linux-aarch64 -f environment.yml
	conda lock --mamba -p osx-64 -p osx-arm64 -p linux-64 -p linux-aarch64 -f predict-environment.yml --filename-template 'predict-{platform}.lock'
