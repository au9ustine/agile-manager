build:
	docker build -t sprint-date-manager .

tests:
	docker run --rm --name sprint-date-manager sprint-date-manager nosetests -s

clean:
	rm -rf *.pyc
	docker images -qa -f dangling=true | xargs --no-run-if-empty docker rmi -f
	docker ps -aq -f status=exited | xargs --no-run-if-empty docker rm

ci: clean build tests
