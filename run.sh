
# Build the Docker images and start the application in the background
echo "Starting containers"
docker compose up --build -d
open http://localhost:8080
echo "Web App launched at: http://localhost:8080"

# Tear-down containers
cleanup(){
    echo "Stopping containers"
    docker compose down
    exit 0
}

trap cleanup INT

echo "Press ctrl + c to stop and clean up."
while :; do
    sleep 1
done

