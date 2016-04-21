build:
	docker build -t sprint_date_manager .

tests: build
	docker run -it sprint_date_manager nosetests -s

clean:
	rm -rf *.pyc
	docker images -qa -f dangling=true | xargs --no-run-if-empty docker rmi -f
	docker ps -aq -f status=exited | xargs --no-run-if-empty docker rm
