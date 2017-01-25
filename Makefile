DOCKER_IMAGE_NAME = au9ustine/manager
COMMIT_HASH = $(shell git rev-parse HEAD)
COMMIT_BRANCH = (shell git symbolic-ref --short HEAD)

build:
	docker build -t sprint-date-manager .

clean:
	rm -rf *.pyc
	docker images -qa -f dangling=true | xargs --no-run-if-empty docker rmi -f
	docker ps -aq -f status=exited | xargs --no-run-if-empty docker rm

ci: clean build tests

# Circle CI
circleci-dependencies:
	docker build -t $(DOCKER_IMAGE_NAME):latest -f docker/Dockerfile.prod .

circleci-pre-test:
	true

circleci-test:
	docker run --rm $(DOCKER_IMAGE_NAME):latest nosetests -s

circleci-deployment:
	docker push $(DOCKER_IMAGE_NAME):latest
