infra:
	docker-compose -f docker-compose.yaml up

run:
	rm -f lfld.log && \
		python withloguru_mock_application.py && \
		rm -f /tmp/lfld.log && \
		cp lfld.log /tmp