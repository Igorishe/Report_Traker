sudo docker run --rm -v postgres_data:/volume -v /tmp:/backup postgres:12.4 tar -cf /backup/test_archive.tar -C /volume ./