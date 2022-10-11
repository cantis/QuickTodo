Write-Output 'killing old docker processes'
docker-compose rm -fs

Write-Output 'Building docker containers'
docker-compose up  --build -d